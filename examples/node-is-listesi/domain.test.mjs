import test from 'node:test';
import assert from 'node:assert/strict';
import { createStore, validateTitle, InputError } from './domain.mjs';

test('başlık boşluğu temizler', () => {
  assert.equal(validateTitle('  Aylık bakım  '), 'Aylık bakım');
});

test('geçersiz başlıkları reddeder', () => {
  for (const value of [null, 4, '', 'ab', 'x'.repeat(81)]) {
    assert.throws(() => validateTitle(value), InputError);
  }
});

test('başlık sınırları dahil kabul edilir', () => {
  assert.equal(validateTitle('abc').length, 3);
  assert.equal(validateTitle('x'.repeat(80)).length, 80);
});

test('iki kayıt farklı kimlik alır', () => {
  const store = createStore();
  const first = store.add({ title: 'Birinci bakım' });
  const second = store.add({ title: 'İkinci bakım' });
  assert.equal(first.id, 1);
  assert.equal(second.id, 2);
});

test('liste kopyası iç kaydı değiştiremez', () => {
  const store = createStore();
  store.add({ title: 'Aylık bakım' });
  const items = store.list();
  items[0].title = 'Dışarıdan değişti';
  items.push({ id: 9 });
  assert.equal(store.list().length, 1);
  assert.equal(store.list()[0].title, 'Aylık bakım');
});

test('tamamlama tekrarı yeni kayıt yaratmaz', () => {
  const store = createStore();
  const job = store.add({ title: 'Arıza kontrolü' });
  assert.equal(store.complete(job.id).done, true);
  assert.equal(store.complete(job.id).done, true);
  assert.equal(store.list().length, 1);
  assert.equal(store.complete(999), null);
});
