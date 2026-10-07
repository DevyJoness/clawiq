import { mkdir, readFile, writeFile, rename, unlink, readdir } from 'node:fs/promises';
import { join } from 'node:path';
import { randomUUID } from 'node:crypto';
export class SessionStore {
  constructor(root) { this.root = root; }
  path(id) {
    if (!/^[a-f0-9-]{36}$/u.test(id)) throw new Error('Invalid session ID');
    return join(this.root, id + '.json');
  }
  async create() {
    const session = { id: randomUUID(), title: 'Новый разговор', updatedAt: new Date().toISOString(), messages: [] };
    await this.save(session); return session;
  }
  async get(id) { return JSON.parse(await readFile(this.path(id), 'utf8')); }
  async save(session) {
    await mkdir(this.root, { recursive: true });
    const target = this.path(session.id), temporary = target + '.' + randomUUID() + '.tmp';
    await writeFile(temporary, JSON.stringify(session, null, 2), { encoding: 'utf8', mode: 0o600 });
    await rename(temporary, target);
  }
  async list() {
    await mkdir(this.root, { recursive: true });
    const files = (await readdir(this.root)).filter(name => /^[a-f0-9-]{36}\.json$/u.test(name));
    const sessions = await Promise.all(files.map(async name => {
      try { const s = await this.get(name.slice(0, -5)); return { id: s.id, title: s.title, updatedAt: s.updatedAt }; }
      catch { return undefined; }
    }));
    return sessions.filter(Boolean).sort((a,b) => b.updatedAt.localeCompare(a.updatedAt));
  }
  async delete(id) { await unlink(this.path(id)); }
}
