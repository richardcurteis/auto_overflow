import string


class Pattern:

    def create_pattern(self, length):
        index_up, index_down, int_index = 0, 0, 0
        int_list = list(range(0, 10))
        char_list = string.ascii_lowercase
        pattern = ''

        while len(pattern) < length:
            if int_index < 9:
                pattern = self.extend_pattern(pattern,
                                              char_list[index_up],
                                              char_list[index_down],
                                              int_list[int_index])
                int_index += 1
            else:
                pattern = self.extend_pattern(pattern,
                                              char_list[index_up],
                                              char_list[index_down],
                                              int_list[int_index])
                int_index = 0

                if index_down <= len(index_down - 1):
                    index_down += 1
                else:
                    index_down = 0
                    index_up += 1

                if index_up <= len(index_down - 1):
                    index_down = 0
        return pattern

    def extend_pattern(self, pattern, upper, lower, integer):
        return pattern + upper.capitalize() + lower + str(integer)



