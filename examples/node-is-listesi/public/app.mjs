const form = document.querySelector('#job-form');
const list = document.querySelector('#jobs');
const message = document.querySelector('#message');
const refresh = document.querySelector('#refresh');
let revision = 0;

async function api(path, options = {}) {
  const response = await fetch(path, options);
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error ?? `HTTP ${response.status}`);
  }
  return data;
}

function render(jobs) {
  const fragment = document.createDocumentFragment();
  for (const job of jobs) {
    const li = document.createElement('li');
    const title = document.createElement('span');
    title.textContent = job.title + (job.done ? ' - Tamamlandı' : '');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = 'Tamamla';
    button.disabled = job.done;
    button.addEventListener('click', async () => {
      button.disabled = true;
      try {
        await api(`/api/jobs/${job.id}/complete`, { method: 'POST' });
        await load();
      } catch (error) {
        message.textContent = error.message;
        button.disabled = false;
      }
    });
    li.append(title, button);
    fragment.append(li);
  }
  list.replaceChildren(fragment);
}

async function load() {
  const current = ++revision;
  message.textContent = 'Yükleniyor...';
  try {
    const jobs = await api('/api/jobs');
    if (current !== revision) return;
    render(jobs);
    message.textContent = jobs.length
      ? `${jobs.length} iş var.` : 'Henüz iş yok.';
  } catch (error) {
    if (current === revision) message.textContent = error.message;
  }
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  const button = form.querySelector('button');
  button.disabled = true;
  try {
    const title = new FormData(form).get('title');
    await api('/api/jobs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    });
    form.reset();
    await load();
  } catch (error) {
    message.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});

refresh.addEventListener('click', load);
load();
