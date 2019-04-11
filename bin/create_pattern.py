import string


class Pattern:

    def create_pattern(self, length):
        index_up, index_down, int_index = 0, 0, 0

        int_list = list(range(0, 10))
        int_limit = 8 #len(int_list)-1 # 8

        char_list = string.ascii_lowercase
        char_limit = len(char_list)-1 # 25

        pattern = ''

        while len(pattern) < length:
            if int_index <= int_limit:
                pattern = pattern + char_list[index_up].capitalize() + char_list[index_down] + str(int_list[int_index])
                int_index += 1

            else:
                int_index = 0

                if index_down <= char_limit:
                    index_down += 1

                if index_down >= char_limit:
                    index_down = 0
                    index_up += 1

                if index_up > char_limit:
                    index_up = 0

        return pattern

    def extend_pattern(self, pattern, upper, lower, integer):
        return pattern + upper.capitalize() + lower + str(integer)



