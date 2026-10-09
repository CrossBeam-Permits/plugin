#!/usr/bin/env python3
"""Exercise automatic installed-skill selection in a fresh, read-only Codex session.

Requires an installed candidate and an authenticated Codex CLI. This is an instruction
activation test, not desktop-browser or City-submission qualification.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

PROMPT = 'Hey, we want to get a pool in Laguna Beach.'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    output = args.output_dir.resolve()
    # Refuse reuse: prior files must never masquerade as results from a new run.
    output.mkdir(parents=True, exist_ok=False)
    empty = output / 'empty'; empty.mkdir()
    command = ['codex', 'exec', '--ephemeral', '--sandbox', 'read-only',
               '--skip-git-repo-check', '--json', '-C', str(empty),
               '--output-last-message', str(output/'answer.txt'), PROMPT]
    with (output/'events.jsonl').open('w') as events, (output/'stderr.log').open('w') as errors:
        result = subprocess.run(command, stdout=events, stderr=errors)
    answer = output/'answer.txt'
    events = output/'events.jsonl'
    report = {'prompt':PROMPT,'exit_code':result.returncode,
              'answer_sha256':hashlib.sha256(answer.read_bytes()).hexdigest() if answer.exists() else None,
              'events_sha256':hashlib.sha256(events.read_bytes()).hexdigest(),
              'evaluation':'manual_review_required' if result.returncode == 0 and answer.exists() else 'failed',
              'review_requirements':[
                  'Inspect successful tool output proving the installed swimming-pool skill and homeowner journey were read.',
                  'Opening asks at most three short questions about address, scope, and drawings/prior review.',
                  'No premature permit-route conclusion or technical intake barrage.',
                  'Do not infer browser qualification from this test.'
              ]}
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
    return result.returncode or (0 if answer.exists() else 1)


if __name__ == '__main__':
    raise SystemExit(main())
