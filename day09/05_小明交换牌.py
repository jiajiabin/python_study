# 小明手里有两张牌，左手红桃A，右手黑桃K，现在小明交换双手的牌，问交换之后，左右手的牌各是什么？

# 牌的类，其对象是单独的牌
class PokerCard:
    def __init__(self, color, size):
        self.color = color          # 花色
        self.size = size            # 大小


# 手的类，用于创建手，手是人的一部分
class Hand:
    card: PokerCard     # 手里可以有一张牌


# 人的类
class Human:
    def __init__(self):             # 人自带两只手
        self.left_hand = Hand()
        self.right_hand = Hand()

    # 人的功能
    # 拿牌
    def catch_cards(self, card1:PokerCard, card2:PokerCard):
        self.left_hand.card = card1
        self.right_hand.card = card2

    # 交换牌
    def swap_cards(self):
        self.left_hand.card, self.right_hand.card = self.right_hand.card,\
                                    self.left_hand.card

    # 展示牌
    def show_cards(self):
        print("左手[%s:%s]" % (self.left_hand.card.color, self.left_hand.card.size))
        print("右手[%s:%s]" % (self.right_hand.card.color, self.right_hand.card.size))



xiaoming = Human()
card1, card2 = PokerCard("红桃", "A"), PokerCard("黑桃", "K")

xiaoming.catch_cards(card1, card2)
xiaoming.show_cards()
xiaoming.swap_cards()
xiaoming.show_cards()


