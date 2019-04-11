import string


class Pattern:

    def create_pattern(self, length):
        index_up, index_down, int_index = 0, 0, 0
        int_list = list(range(0, 10))
        char_list = string.ascii_lowercase
        pattern = ''

        while len(pattern) < length:
            if int_index <= 9:
                pattern = pattern + char_list[index_up].capitalize() + char_list + str(int_list[int_index])
                int_index += 1

            else:
                int_index = 0

                if index_down <= len(char_list):
                    index_down += 1
                else:
                    index_down = 0
                    index_up += 1

                if index_up <= len(char_list):
                    index_down = 0
        return pattern

    def extend_pattern(self, pattern, upper, lower, integer):
        return pattern + upper.capitalize() + lower + str(integer)



