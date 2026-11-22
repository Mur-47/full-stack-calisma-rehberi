export class InputError extends Error {}

export function validateTitle(value) {
  if (typeof value !== 'string') {
    throw new InputError('Başlık metin olmalı.');
  }
  const title = value.trim();
  if (title.length < 3 || title.length > 80) {
    throw new InputError('Başlık 3-80 karakter olmalı.');
  }
  return title;
}

export function createStore() {
  let nextId = 1;
  const jobs = [];
  const copy = job => ({ ...job });

  return {
    list() {
      return jobs.map(copy);
    },
    add(input) {
      const title = validateTitle(input?.title);
      const job = { id: nextId++, title, done: false };
      jobs.push(job);
      return copy(job);
    },
    complete(id) {
      const job = jobs.find(item => item.id === id);
      if (!job) return null;
      job.done = true;
      return copy(job);
    }
  };
}
