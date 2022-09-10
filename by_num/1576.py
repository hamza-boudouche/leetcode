class Solution:
    def modifyString(self, s: str) -> str:
        letters = []
        letters[:] = s
        spare_letters = ["a", "b", "c", "d"]
        i = 0
        while i < len(s):
            if letters[i] == "?":
                if i == len(s) - 1:
                    # take one letter from spare letters that's different from letters[i-1]
                    for letter in spare_letters:
                        if letter != letters[i-1]:
                            letters[i] = letter
                            i += 1
                            break
                else:
                    # we may have more than one "?"
                    # loop to find the end
                    end = i
                    while end < len(s) - 1 and letters[end] == "?":
                        end += 1
                    # pick the spare letters
                    used_spare_letters = []
                    for letter in spare_letters:
                        if len(used_spare_letters) == 2:  # we only need 2 spare letters
                            break
                        if i == 0:  # need to check only against one letter
                            if letter != letters[end]:
                                used_spare_letters.append(letter)
                        else:  # need to check against 2 letters
                            if letter != letters[i-1] and letter != letters[end]:
                                used_spare_letters.append(letter)
                    # start replacing
                    parity_number = 0  # to switch between the 2 chosen spare letters
                    for j in range(i, end):
                        letters[j] = used_spare_letters[parity_number]
                        parity_number = 1 - parity_number
                    if end == len(s) - 1:
                        i = end
                    else:
                        i = end + 1
            else:
                i += 1
        s = "".join(letters)
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.modifyString("???"))
