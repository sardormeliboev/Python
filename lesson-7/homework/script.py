
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#
  def digit_sum(k):
    return sum(map(int, str(k)))

print(digit_sum(24))
print(digit_sum(502))  
#
def powers_of_two(N):
    result = []
    power = 1
    while 2 ** power <= N:
        result.append(2 ** power)
        power += 1
    return result
print(powers_of_two(10)) 
