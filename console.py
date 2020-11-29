import pdb

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository 

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

groceries = Tag("Groceries")
tag_repository.save(groceries)

entertainment = Tag("Entertainment")
tag_repository.save(entertainment)

bills = Tag("Bills")
tag_repository.save(bills)

eating_out = Tag("Eating out")
tag_repository.save(eating_out)

personal_care = Tag("Personal care")
tag_repository.save(personal_care)

gifts = Tag("Gifts")
tag_repository.save(gifts)

tesco = Merchant("Tesco")
merchant_repository.save(tesco) 

landlord = Merchant("Landlord")
merchant_repository.save(landlord)

asda = Merchant("Asda")
merchant_repository.save(asda) 

gft = Merchant("Glasgow Film Theatre")
merchant_repository.save(gft)

amazon = Merchant("Amazon")
merchant_repository.save(amazon)

trans_1 = Transaction(12.30, tesco, groceries)
transaction_repository.save(trans_1)

trans_2 = Transaction(5.30, asda, groceries)
transaction_repository.save(trans_2)

trans_3 = Transaction(15.00, amazon, gifts)
transaction_repository.save(trans_3)

trans_4 = Transaction(10.10, amazon, personal_care)
transaction_repository.save(trans_4)


pdb.set_trace()