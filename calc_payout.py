import sys


#Calculates an even dispersal between winners in the fantasy league
def main():
    """
    calc_payout.py <individual dues> <num teams> <num winners>
    """
    if len(sys.argv) != 4:
        print main.__doc__
    else:
        dues = int(sys.argv[1])
        num_teams = int(sys.argv[2])
        num_winners = int(sys.argv[3])
        interval = ((dues * num_teams) - (dues * num_winners)) / (num_winners * (num_winners -1) * 0.5)
        for winner in range(0, num_winners):
            print "{} Place: ${}".format(winner + 1, dues + (num_winners - winner - 1) * interval)

if __name__ == "__main__":
    main()
        
        
