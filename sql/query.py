from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import Session
import config

# from config import connection

def main():
    print("Welcome to the database.")

    # set up sqlalchemy session
    engine = create_engine(f"postgresql+psycopg2://{config.user}:{config.password}@{config.host}:{config.port}/{config.dbname}")
    session = Session(engine)

    entry = ''
    while True:
        entry = input("What information would you like to extract? Enter respective keys listed below \n"
                       "1: Enter 1 - TKH Instagram post with the highest number of interactions \n"
                       "2: Enter 2 - TKH Youtube video with the highest number of interactions\n"
                       "3: Enter 3 - Return the average number of interactions across all platforms.\n"
                       "E: Exit ")
        
        result = ''
        if entry == '1':
            result = session.query(func.market.max_youtube_inter()).all()
        elif entry == '2':
            result = session.query(func.market.market.instagram_interactions()).all()
        elif entry == '3':
           result = session.query(func.market.total_interactions()).all()
        elif entry == 'E':
            print("Exiting")
            break
        else:
            print("Unrecognized key. Try again.")

        print(result)
    
if __name__ == "__main__":
    main()