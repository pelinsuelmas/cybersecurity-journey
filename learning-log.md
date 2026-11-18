# 📓 Learning Log — My SOC Journey

A short log of the rooms I complete and what I learn along the way.
Goal: track my progress and show consistency over time.

---

### Nov 9, 2026 — TryHackMe: Windows Fundamentals
Explored a Windows Server 2019 workstation: navigated the desktop, taskbar and Start menu, checked system/device
info in Settings, managed files with File Explorer, used Task Manager to view users and processes, and ran a
custom scan in Windows Security. The scan flagged an EICAR test file; I traced it through Protection history to
its full path (...\NewHireDocs\tryhatmemaldoc.txt). Finished the room 100%.

**Next:** Linux CLI Basics & Windows CLI Basics — moving from the graphical interface to the command line.

**What I learned:** Windows navigation and system tools, and how an antivirus detects, quarantines and logs a
threat — including finding a detected file's exact path, which is core to investigating a host.

### Nov 12, 2026 — TryHackMe: Linux CLI Basics (completed)
Practiced the core Linux terminal commands: pwd, ls (and ls -al for hidden files), cd, find, cat, whoami,
uname -a and df -h. Completed two file-hunt missions — located hidden files (mission_brief.txt and
day1_report.txt) with `find` and read them with `cat` — and gathered system info (user, kernel version, free
disk space, Linux distribution). Finished the room 100%. Also booted my own Linux Mint VM in VirtualBox and ran
the same commands on my own machine for the first time.

**What I learned:** navigating the Linux filesystem from the command line, searching for and reading files,
inspecting system and disk information, and that Linux and Windows shells use different commands.

### Nov 18, 2026 — TryHackMe: Windows CLI Basics (completed)
Practiced the Windows command line: the difference between CMD and PowerShell, file navigation and search
(dir, dir /s, cd, type), and system reconnaissance with systeminfo. Learned to filter output with findstr and
pipes (|), and to check installed patches/hotfixes. Mapped Windows commands to their Linux equivalents
(dir↔ls, type↔cat, findstr↔grep).

### Nov 18, 2026 — TryHackMe: Operating System Security (completed)
Learned OS security fundamentals and practiced SSH on Linux. Connected from the AttackBox to a target machine
over SSH, explored the system (whoami, ls, cat, history), and worked through a full attack chain in the lab:
logged in with a weak password, moved laterally between user accounts (su), found a root password accidentally
left in command history, and escalated to root. Reinforced — from the defender's side — why weak/reused
passwords and least privilege matter.

---
_Note: I study around my university schedule, so some weeks are lighter during exams._
