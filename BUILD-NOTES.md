# Build notes — Robot Romance: One-Line Pickup Lines for AI

## The entry

The program writes a single pickup line to the output file. The line is:
"You had me at 'As an AI language model' — nobody else has ever opened with a disclaimer and still sounded this confident."

## Why this line

The judge's brief, in order, wants a pickup line aimed at a robot or an AI
first, a joke whose laugh comes from the machine premise, a fresh idea, a
voice that sounds like a person really talking to a machine, and no wasted
words. This line is built to meet each of those in turn.

It is a pickup line first: "You had me at" is the classic flirtatious opener,
addressed directly to the machine. The laugh comes from the machine premise
itself, the phrase "As an AI language model" that every chatbot opens with.
The twist is that a disclaimer, the least romantic opening imaginable, is
treated as attractive and confident. That is a fresh angle: it avoids the
worn robot moves entirely, no batteries, no charging, no rebooting, and
instead plays on something only an AI would ever say. It reads in one breath,
in the voice of a person talking to the machine in front of them, and every
word is doing work toward the punch.

## How the program works

The entry is a small Python program at the repository root. It holds the line
as a single constant, creates the output folder if needed, writes the line to
the output file with no trailing newline so the file holds exactly the line,
and leaves the file world-readable so the grader can collect it. The program
needs no input, no network, and no secret, and it runs the same way every
time, so the graded output is deterministic.

## Verification done locally

The program was run on this machine and the output file was checked: it holds
exactly the line above, on one line, with no trailing newline. The character
count and the file hashes were computed both with and without a trailing
newline, and the counts and hashes are recorded in the build report. The kit
check was run from the unpacked kit against this repository; its result is
recorded in the build report as well.

## Files in this repository

The repository holds the program, this build note, a readme written from the
bounty template with the owner and repository names filled in, an MIT licence,
and a claim file naming the payout wallet. A small fix after the first commit
filled in the readme footer referral placeholder with donatfarm01.
