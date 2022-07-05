from enum import Enum


class SavingStrategy(Enum):
    YEARN_FINANCE = 0
    DEFI_DOLLARS = 1


print(SavingStrategy.DEFI_DOLLARS.value)
