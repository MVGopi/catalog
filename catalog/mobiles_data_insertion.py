from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from mobiles_database_setup import *

db_engine = create_engine('sqlite:///mobiles_store.db')

# For accessing declaratives through Database_Session instance need
# to  bind the db_engine to metadata of base class
Base.metadata.bind = db_engine


Database_Session = sessionmaker(bind=db_engine)
# Database_Session() instance establishes conversations with database

session = Database_Session()

# delete users if any existed
session.query(User).delete

# delete companies if already existed in company table
session.query(Company).delete()

# delete mobiles data if already existed in the mobile table
session.query(Mobile).delete()

# insert one user record
user = User(name="venkata gopi", email="venkatagopi894@gmail.com",
            picture="https://drive.google.com/drive/folders/"
                    "0B-DCot06UZdQcHZ4ajVic1hRQjQ")
session.add(user)

# insert some of the companies
m = Company(name="Motorola", user_id=1, icon="https://cdn6.aptoide.com/"
            "imgs/d/9/4/d942039af19526adaa8c2047a7af21af_icon.png?w=256")
o = Company(name="Oppo", user_id=2,
            icon="https://cdn6.aptoide.com/imgs/d/9/4/"
            "d942039af19526adaa8c2047a7af21af_icon.png?w=256")
s = Company(name="Samsung", user_id=3,
            icon="https://mostvaluablebrands.com/wp-content/"
            "uploads/2016/03/samsung-logo.jpg")
a = Company(name="Apple", user_id=4,
            icon="https://images-na.ssl-images-amazon.com/"
                 "images/I/218MZ3obWgL.jpg")
session.add(m)
session.add(o)
session.add(s)
session.add(a)
session.commit()

# insert some mobiles data
Motog5S_plus = Mobile(name="MotoG5S-Plus", price="16000INR", ram="4GB",
                      rom="64GB", front_cam="5mp", back_cam="13mp",
                      image="https://images-na.ssl-images-amazon.com/"
                      "images/I/91iEQO5Kl1L._SY355_.jpg", company_id=1)
Oppo_F7 = Mobile(name="Oppo_F7", price="19,990INR", ram="4GB", rom="64GB",
                 front_cam="25mp", back_cam="16mp",
                 image="https://www.91-img.com/pictures/125850-v5-oppo-f7-"
                 "mobile-phone-large-1.jpg", company_id=2)
Samsung_GalaxyM20 = Mobile(name="Samsung_GalaxyM20", price="12,990INR",
                           ram="4GB", rom="64GB", front_cam="5mp",
                           back_cam="13mp", image="https://techwafer.com/"
                           "wp-content/uploads/2019/01/Samsung-Galaxy-M20-"
                           "price-in-Pakistan-600x600.jpg", company_id=3)
Apple_XSMax = Mobile(name="Apple_XSMax", price="119,990INR", ram="4GB",
                     rom="256GB", front_cam="12mp", back_cam="12mp",
                     image="https://encrypted-tbn0.gstatic.com/images?q="
                     "tbn:ANd9GcQUEEpPnwWju9UaR3N8EucqxPt5vf4qyRsG9mpBRm3"
                     "Jgf-JaOZM", company_id=4)
session.add(Motog5S_plus)
session.add(Oppo_F7)
session.add(Samsung_GalaxyM20)
session.add(Apple_XSMax)
session.commit()

print("Data given by you has been inserted")
