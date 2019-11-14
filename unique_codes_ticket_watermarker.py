import os, argparse, sys
from ticket_unique_code_generator import TicketUniqueCodeGenerator
from picture_watermarker import PictureWatermarker

class UniqueCodesTicketWatermarker:
    # Gets ticket design image and replicates it number of times and applies
    # unique ticket code to it

    def __init__(self, image_path, number_of_tickets):
        self.image_path = image_path
        self.number_of_tickets = number_of_tickets

    def call(self):
        if not os.path.exists('export'):
            os.makedirs('export')

        unique_codes = TicketUniqueCodeGenerator.generate_codes(self.number_of_tickets)
        watermarker = PictureWatermarker()
        for code in unique_codes:
            watermarker.watermark_picture(self.image_path, code)

if __name__ == "__main__":
    # UniqueCodesTicketWatermarker("./picture.jpg", 3).call()
    parser = argparse.ArgumentParser(description='Unique Codes Picture Watermarker')
    parser.add_argument('image_path', metavar='image_path', nargs=1, help='Image path')
    parser.add_argument('number_of_tickets', metavar='number_of_tickets', nargs=1, help='Number of tickets that will be generated with unique codes', type=int)
    args = parser.parse_args()

    print "-- Unique Codes Picture Watermarker v1.0 --"
    print "Use -h for help. \n"
    for k,v in sorted(args.__dict__.iteritems()):
        print "{0}: {1}".format(k,v)

    answer = raw_input('\nProceed with presented arguments? [y\\n]')
    if answer.strip().lower() == 'y':
        print args
        UniqueCodesTicketWatermarker("./" + args.image_path[0], args.number_of_tickets[0]).call()
    else:
        sys.exit()
