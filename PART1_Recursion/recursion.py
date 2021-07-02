def count_even_odd_recursive(string):

    def helper(helper_input):
        if len(helper_input) == 0:
            return 0, 0

        odd, even = helper(helper_input[1:])

        if int(helper_input[0]) % 2 == 0:
            even += 1
        else:
            odd += 1

        return odd, even

    odd, even = helper(string)

    if even > odd:
        return f'There are more even numbers ({even}) that odd ({odd}).'
    else:
        return f'There are more odd numbers ({odd}) or the same as even numbers ({even}).'


print(count_even_odd_recursive("0987650"))

