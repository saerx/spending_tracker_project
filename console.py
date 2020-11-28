import pdb

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository 

from models.transaction import Transaction
# import repositories.transaction_repository as transaction_repository

# transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Entertainment")
tag_repository.save(tag_2)

tag_3 = Tag("Bills")
tag_repository.save(tag_3)

merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1) 

merchant_2 = Merchant("landlord")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Asda")
merchant_repository.save(merchant_3) 

merchant_4 = Merchant("Glasgow Film Theatre")
merchant_repository.save(merchant_4)


pdb.set_trace()