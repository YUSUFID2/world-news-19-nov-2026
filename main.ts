// world-news-19-nov-2026 — make.fun news-image-20261119 entry.
//
// One image summing up the world's news of Thursday 19 November 2026:
// the Trump–Xi–Putin trilateral summit in Shenzhen, the global rollout
// of GTA VI, Anthropic's record $81.3B IPO, and NASA's Voyager 1
// reaching one light-day from Earth.
//
// This program copies the finished entry image (entry.png, a JPEG
// under 1 MiB at 1024x1024) into the output directory. Node 22,
// standard library only, no network.
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Node runs .ts files as ES modules, where __dirname does not exist,
// so derive the script's directory from its own URL instead.
const __dirname = dirname(fileURLToPath(import.meta.url));

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(join(__dirname, "entry.png"), dest);
console.log(`wrote ${dest} (${statSync(dest).size} bytes)`);
