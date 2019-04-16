Basic script for fuzzing and enumerating a service for vanilla 32-bit buffer overflows.
The script automates sending the incremental block of 'A's and then creating a non-sequential pattern based on the point at which a crash is detected.
From there the user is able to input the overwritten hex value from EIP and the script will find the offset.

Essentiall a copy of the functionalit provided by Metasploit's `create_pattern.rb` and `pattern_offset.rb`.

This just part of OSCP study and will hopefully be useful for automating some enumeration if required.

I'll look to add a loop for automatically targeting the exact EIP overload point without human input. We shall see!
