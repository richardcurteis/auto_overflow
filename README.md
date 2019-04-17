Basic script for fuzzing and enumerating a service for vanilla 32-bit buffer overflows.
The script automates sending the incremental block of 'A's and then creating a non-sequential pattern based on the point at which a crash is detected.
From there the user is able to manually (for now) input the overwritten hex value from EIP and the script will find the offset.

Essentially this is a copy of the functionality provided by Metasploit's `create_pattern.rb` and `pattern_offset.rb`.

This just part of OSCP study and will hopefully be useful for automating some enumeration if required. Mostly it is just for me to properly look at the BO mecahnics and practice my Python on a tangible project.

User just nees to enter EIP value and restart vulnserver manually.

I'll look to add a loop for automatically targeting the exact EIP overload point without human input. We shall see!

Eventually with some modification of Mona it should in theory be possible to automate the full lifecycle including finding unprotected memory locations for JMP points, identifying bad characters etc.
