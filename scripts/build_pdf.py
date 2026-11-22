from pathlib import Path
import re, sys, json, html, textwrap, unicodedata
ROOT=Path(__file__).resolve().parents[1]

from reportlab.platypus import (BaseDocTemplate,PageTemplate,Frame,Paragraph,
    Spacer,PageBreak,Flowable,KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
W,H=A4
M=48
INK=colors.HexColor('#153c34')
ACCENT=colors.HexColor('#b4ce87')
BODY=colors.HexColor('#25352f')
font_dir=Path(__import__('os').environ.get('BOOK_FONT_DIR','C:/Windows/Fonts'))
if not font_dir.exists():
    font_dir=Path('/usr/share/fonts/truetype/dejavu')
if not font_dir.exists():
    raise RuntimeError('Arial veya DejaVu font klasörü bulunamadı; BOOK_FONT_DIR ayarlayın.')
for name,file in [('Body','arial.ttf'),('Bold','arialbd.ttf'),
                  ('Italic','ariali.ttf'),('Mono','consola.ttf')]:
    if not (font_dir/file).exists():
        file={'Body':'DejaVuSans.ttf','Bold':'DejaVuSans-Bold.ttf','Italic':'DejaVuSans-Oblique.ttf','Mono':'DejaVuSansMono.ttf'}[name]
    pdfmetrics.registerFont(TTFont(name,str(font_dir/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
styles={
 'body':ParagraphStyle('BodyTextBook',fontName='Body',fontSize=10.2,
     leading=15.3,textColor=BODY,spaceAfter=8.5,allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('Chapter',fontName='Bold',fontSize=22,leading=27,
     textColor=INK,spaceAfter=17,keepWithNext=True),
 'h2':ParagraphStyle('Section',fontName='Bold',fontSize=14,leading=18,
     textColor=INK,spaceBefore=13,spaceAfter=8,keepWithNext=True),
 'h3':ParagraphStyle('Subsection',fontName='Bold',fontSize=11.4,leading=15,
     textColor=INK,spaceBefore=8,spaceAfter=5,keepWithNext=True),
 'bullet':ParagraphStyle('BulletBook',fontName='Body',fontSize=10.2,
     leading=15.3,textColor=BODY,leftIndent=13,firstLineIndent=-10,
     spaceAfter=6,allowWidows=0,allowOrphans=0),
 'note':ParagraphStyle('NoteBook',fontName='Body',fontSize=9.6,leading=14.3,
     textColor=INK,borderColor=ACCENT,borderWidth=.6,borderPadding=10,
     backColor=colors.HexColor('#f3f7ed'),spaceBefore=7,spaceAfter=12),
 'source':ParagraphStyle('SourceBook',fontName='Body',fontSize=9.2,
     leading=12.8,textColor=colors.HexColor('#536b60'),spaceAfter=5.5,
     allowWidows=0,allowOrphans=0),
}
def clean(s):
    return unicodedata.normalize('NFC',s).replace('\ufeff','').replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
def inline(s):
    s=clean(s)
    tokens={}
    def stash(value):
        key='ZZTOKEN'+str(len(tokens))+'ZZ';tokens[key]=value;return key
    s=re.sub(r'`([^`]+)`',lambda m:stash('<font name="Mono" size="9.1" color="#234e43">'+html.escape(m[1])+'</font>'),s)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^ )]+)\)',lambda m:stash('<link href="'+html.escape(m[2],quote=True)+'" color="#1f6956">'+html.escape(m[1])+'</link>'),s)
    s=html.escape(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    # Bare official links stay readable and clickable; long links can break.
    s=re.sub(r'https?://[^\s<>]+',lambda m:'<link href="'+m[0]+'" color="#1f6956">'+m[0]+'</link>',s)
    for k,v in tokens.items():s=s.replace(k,v)
    return s

class CodeBlock(Flowable):
    def __init__(self,lines,lang='',continued=False):
        super().__init__();self.lines=lines;self.lang=lang;self.continued=continued
        self.font=8.0;self.leading=11.5;self.pad=12;self.top=24 if lang else 11
    def wrap(self,availWidth,availHeight):
        self.width=availWidth
        self.drawlines=[]
        for raw in self.lines:
            raw=clean(raw.expandtabs(4))
            # Font is reduced a little for very long single shell commands.
            maxcols=int((availWidth-2*self.pad)/(self.font*.55))
            pieces=textwrap.wrap(raw,width=maxcols,replace_whitespace=False,
                drop_whitespace=False,break_long_words=True,break_on_hyphens=False) or ['']
            self.drawlines.extend(pieces)
        self.height=self.top+len(self.drawlines)*self.leading+self.pad
        return self.width,self.height
    def split(self,availWidth,availHeight):
        self.wrap(availWidth,availHeight)
        n=int((availHeight-self.top-self.pad)/self.leading)
        if n<3:return []
        # Already visually wrapped lines; source files preserve exact original.
        return [CodeBlock(self.drawlines[:n],self.lang,self.continued),
                CodeBlock(self.drawlines[n:],self.lang,True)]
    def draw(self):
        c=self.canv;c.setFillColor(colors.HexColor('#f2f5f4'))
        c.setStrokeColor(colors.HexColor('#d9e3de'))
        c.roundRect(0,0,self.width,self.height,5,fill=1,stroke=1)
        if self.lang:
            c.setFont('Bold',7.6);c.setFillColor(colors.HexColor('#557468'))
            label=self.lang.upper()+(' / DEVAM' if self.continued else '')
            c.drawString(self.pad,self.height-14,label)
        c.setFont('Mono',self.font);c.setFillColor(colors.HexColor('#173c32'))
        y=self.height-self.top
        for line in self.drawlines:
            c.drawString(self.pad,y,line);y-=self.leading

class Cover(Flowable):
    def __init__(self):super().__init__();self.width=W-2*M;self.height=H-2*M-2
    def draw(self):
        c=self.canv;c.setFillColor(INK);c.rect(-M,-M,W,H,fill=1,stroke=0)
        c.setFillColor(ACCENT);c.rect(0,self.height-48,56,5,fill=1,stroke=0)
        c.setFillColor(colors.white);c.setFont('Bold',11)
        c.drawString(0,self.height-81,'TÜRKÇE UYGULAMALI ÇALIŞMA KİTABI')
        c.setFont('Bold',12)
        c.drawString(0,self.height-103,'Hazırlayan: Murat AKTAŞ')
        title=Paragraph('Sıfırdan<br/>Full Stack<br/>Geliştiriciliğe',ParagraphStyle('CoverTitle',fontName='Bold',fontSize=40,leading=47,textColor=colors.white))
        tw,th=title.wrap(self.width-8,240);title.drawOn(c,0,self.height-123-th)
        sub=Paragraph('Kodu oku. Elle yaz. Hata üret.<br/>Kanıtla, düzelt, yeniden dene.',ParagraphStyle('CoverSub',fontName='Body',fontSize=17,leading=25,textColor=ACCENT))
        sw,sh=sub.wrap(self.width-10,100);sub.drawOn(c,0,self.height-380-sh)
        c.setStrokeColor(colors.HexColor('#416457'));c.line(0,157,self.width,157)
        p=Paragraph('Git / GitHub / HTML / CSS / JavaScript / Node.js<br/>C# / ASP.NET Core / SQL / ORM / EF Core<br/>Docker / Compose / Caddy / Test / Güvenlik / Debug',ParagraphStyle('CoverTools',fontName='Body',fontSize=10.5,leading=18,textColor=colors.white))
        pw,ph=p.wrap(self.width,100);p.drawOn(c,0,76)
        c.setFont('Body',9);c.setFillColor(ACCENT)
        c.drawString(0,30,'22 Kasım 2026  |  24 haftalık rota ve bitirme projesi')

class BookDoc(BaseDocTemplate):
    def __init__(self,path):
        super().__init__(str(path),pagesize=A4,leftMargin=M,rightMargin=M,
            topMargin=49,bottomMargin=48,title='Sıfırdan Full Stack Geliştiriciliğe',
            author='Murat AKTAŞ (Mur-47)',
            subject='JavaScript, Node.js, Git, GitHub, Docker, .NET ve EF Core')
        self.addPageTemplates(PageTemplate(id='book',frames=[Frame(M,48,W-2*M,H-97,id='normal',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.header))
        self.chapter='Çalışma kitabı';self.bookmarkseq=0
    def beforeDocument(self):
        self.bookmarkseq=0
        self.chapter='Çalışma kitabı'
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and hasattr(f,'_booklevel'):
            level=f._booklevel;text=f.getPlainText();self.bookmarkseq+=1
            key='item'+str(self.bookmarkseq);self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text,key,level,False)
            if level==0:self.notify('TOCEntry',(0,text,self.page,key))
            if level==0:self.chapter=text

def header(self,c,doc):
    if doc.page==1:return
    c.saveState();c.setStrokeColor(colors.HexColor('#d8e2dc'));c.line(M,H-32,W-M,H-32)
    c.setFont('Body',8);c.setFillColor(colors.HexColor('#5f756a'))
    title='Uygulamalı full stack / Oku, yaz, hata ayıkla'
    while pdfmetrics.stringWidth(title,'Body',8)>W-2*M-30:title=title[:-2]
    c.drawString(M,H-24,title);c.drawString(M,27,'FULL STACK ÇALIŞMA KİTABI')
    c.setFont('Bold',9);c.drawRightString(W-M,27,str(doc.page));c.restoreState()
BookDoc.header=header

def parse_markdown(text,story,counter):
    lines=clean(text).splitlines();i=0;paragraph=[]
    def flush():
        if paragraph:
            text=' '.join(paragraph)
            style=styles['source'] if 'https://' in text and len(text.split())<80 else styles['body']
            story.append(Paragraph(inline(text),style));paragraph.clear()
    while i<len(lines):
        line=lines[i]
        if line.startswith('```'):
            flush();lang=line[3:].strip();i+=1;code=[]
            while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
            story.append(CodeBlock(code,lang));story.append(Spacer(1,10));i+=1;continue
        m=re.match(r'^(#{1,4})\s+(.*)',line)
        if m:
            flush();level=len(m[1]);title=m[2]
            if level==1:
                if counter[0]>0:story.append(PageBreak())
                counter[0]+=1;label=f'{counter[0]:02d}  {title}'
                p=Paragraph(inline(label),styles['h1']);p._booklevel=0
            else:
                p=Paragraph(inline(title),styles['h2' if level==2 else 'h3']);p._booklevel=1
            story.append(p);i+=1;continue
        if not line.strip():flush();i+=1;continue
        if re.match(r'^\s*[-*]\s+',line):
            flush();s=re.sub(r'^\s*[-*]\s+','',line);story.append(Paragraph('• '+inline(s),styles['source'] if 'https://' in s else styles['bullet']));i+=1;continue
        if re.match(r'^\d+[.)]\s+',line):
            flush();story.append(Paragraph(inline(line),styles['bullet']));i+=1;continue
        if line.startswith('>'):
            flush();note=[]
            while i<len(lines) and lines[i].startswith('>'):note.append(lines[i].lstrip('> '));i+=1
            story.append(Paragraph(inline(' '.join(note)),styles['note']));continue
        if re.match(r'^\s*[-*_]{3,}\s*$',line):flush();story.append(Spacer(1,12));i+=1;continue
        paragraph.append(line.strip());i+=1
    flush()

def main():
    out=ROOT/'pdf/full-stack-calisma-rehberi.pdf'
    parts=sorted((ROOT/'book').glob('[0-9][0-9]-*.md'))
    story=[Cover(),PageBreak()]
    story.append(Paragraph('İçindekiler',styles['h1']))
    story.append(Paragraph('Bölüm adları tıklanabilir. PDF okuyucunuzun yer imleri panelinde alt başlıklar da bulunur.',styles['body']))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC1',fontName='Body',fontSize=10.2,leading=16.5,spaceBefore=4,leftIndent=0,firstLineIndent=0,rightIndent=26)]
    story.append(toc);story.append(PageBreak())
    counter=[0]
    for p in parts:parse_markdown(p.read_text(encoding='utf-8'),story,counter)
    doc=BookDoc(out);doc.multiBuild(story)
    reader=PdfReader(str(out));words=sum(len(p.read_text(encoding='utf-8').split()) for p in parts)
    print(json.dumps({'pdf':str(out),'pages':len(reader.pages),'chapters':counter[0],'words':words,'bytes':out.stat().st_size},ensure_ascii=False))

if __name__=='__main__':main()
