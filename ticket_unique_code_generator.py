import base32_crockford, random

class TicketUniqueCodeGenerator:

    @classmethod
    def generate_code(cls):
        return base32_crockford.encode(random.randint(2**25, 3**18), split=3)

    @classmethod
    def generate_codes(cls, number_of_codes):
        return list(set([cls.generate_code() for code in range(number_of_codes)]))
