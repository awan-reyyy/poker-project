import random
import tkinter as tk
from PIL import Image

class Card (object):
  ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  suits = ('♠','♢', '♣', '♡')

  def __init__ (self, rank, suit):
    '''This sets up how our functions will be imported'''
    self.rank = rank
    self.suit = suit

  def __str__ (self):
    ''' Assigns value to card names'''
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)
   

class Deck (object):
  def __init__ (self):
    ''' Takes suits ranks and builds decks'''
    self.deck = []
    for suit in Card.suits:
      for rank in Card.ranks:
        card = Card (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    '''This module changes the order of elements'''
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_inHands):
    self.deck = Deck()
    self.deck.shuffle ()
    self.hands = []
    self.tlist=[]       
    numofCards_in_Hand = 5

    for i in range (num_inHands):
      hand_value = []
      for j in range (numofCards_in_Hand):
        hand_value.append (self.deck.deal())
      self.hands.append (hand_value)
  

  def deck_builder (self):
    '''This function takes in cards and prints the name and suites of those cards'''
    for i in range (len (self.hands) ):
      sort_Hand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sort_Hand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)


  def partial_score (self,hand):                
    '''This function calculates the partial score'''
    sort_Hand=sorted(hand,reverse=True)
    card_sum =0
    rankOfList=[]
    for card in sort_Hand:
      rankOfList.append(card.rank)
    card_sum = rankOfList[0]*13**4+rankOfList[1]*13**3+rankOfList[2]*13**2+rankOfList[3]*13+rankOfList[4]
    return card_sum


  def check_Royal (self, hand):
    '''This function takes in Card rank as well as suites, and checks if all the card are Royal Flush or not. Eg. 10JKQA in same suite is a Royal Flush. Return total point, and print 'Royal Flush' if true, passes down to Check_StraightFlush, if False'''
    sort_Hand=sorted(hand,reverse=True)
    Check =True
    hand = 10
    Card_suit = sort_Hand[0].suit
    Card_rank=14
    count=hand*13**5+self.partial_score(sort_Hand)
    for card in sort_Hand:
      if card.suit!=Card_suit or card.rank!=Card_rank:
        Check =False
        break
      else:
        Card_rank-=1
    if Check:
        print('Royal Flush!!!!')
        self.tlist.append(count)    
    else:
      self.Check_StraightFlush(sort_Hand)
    


  def Check_StraightFlush (self, hand): 
    """This function checks if there is a straight flush in a players' hand.
    : e.g. 4H 5H 6H 7H 8H (H --> Hearts)
    """     
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=9
    Card_suit=sort_hand[0].suit
    Card_rank=sort_hand[0].rank
    count=hand*13**5+self.partial_score(sort_hand)
    for card in sort_hand:
      if card.suit!=Card_suit or card.rank!=Card_rank:
        check=False
        break
      else:
        Card_rank-=1
    if check:
      print ('Straight Flush!')
      self.tlist.append(count)
    else:
        self.Check_Four(sort_hand)



  def Check_Four (self, hand):
    """This function Checks if there are four cards of the same type."""
    sort_hand=sorted(hand,reverse=True)
    Check=True
    hand=8
    Card_rank=sort_hand[1].rank               
    #since it has 4 identical ranks,the 2nd one in the sorted list must be the identical rank
    total_point=0
    count=hand*13**5+self.partial_score(sort_hand)
    for card in sort_hand:
      if card.rank==Card_rank:
        total_point+=1
    if not total_point <4:
      Check = True
      print('Four of a Kind')
      self.tlist.append(count)
    else:
        self.Check_Full(sort_hand)



  def Check_Full (self, hand):  
    ''' Checks if the hand contains three cards of one rank and two cards of another rank. Eg: 66633'''                   
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=7
    count=hand*13**5+self.partial_score(sort_hand)
    mylist=[]                                 #creates a list to store ranks
    for card in sort_hand:
      mylist.append(card.rank)
    rank_one=sort_hand[0].rank                  #The 1st rank and the last rank should be different in a sorted list
    rank_two=sort_hand[-1].rank
    count_rank1=mylist.count(rank_one)
    count_rank2=mylist.count(rank_two)
    if (count_rank1==2 and count_rank2==3)or (count_rank1==3 and count_rank2==2):
      check=True
      print ('Full House')
      self.tlist.append(count)     
    else:
      self.Check_Flush(sort_hand)



  def Check_Flush (self, hand):
    """This function takes in the card numbers as well as suites. Checks if there 
    :are five cards of the same suite, returns the count and prints 'Flush' if true, passes down to Check_Straight() if false"""                             
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=6
    count= hand*13**5+self.partial_score(sort_hand)
    Card_suit=sort_hand[0].suit
    for card in sort_hand:
      if not(card.suit==Card_suit):
        check=False
        break
    if check:
      print ('Flush ♠♢♣♡')
      self.tlist.append(count)    
    else:
      self.Check_Straight(sort_hand)



  def Check_Straight (self, hand):
    """This function checks if all the cards in a players' hand come consecutively in rank or not, returns True if comes consecutively.
    : e.g. 4H 5S 6H 7D 8A (H --> Hearts)""" 
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=5 
    count=hand*13**5+self.partial_score(sort_hand)
    card_rank = sort_hand[0].rank                        #this should be the highest rank
    for card in sort_hand:
      if card.rank!=card_rank:
        check=False
        break
      else:
        card_rank-=1
    if check:
      print('Straight')
      self.tlist.append(count)
    else:
      self.Check_Three(sort_hand)



  def Check_Three (self, hand):
    """This function checks if there are three cards of the same rank. 
    : e.g. KKK23"""
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=4
    count=hand*13**5+self.partial_score(sort_hand)
    card_rank=sort_hand[2].rank                    #In a sorted rank, the middle one should have 3 counts if check=True
    mylist=[]
    for card in sort_hand:
      mylist.append(card.rank)
    if mylist.count(card_rank)==3:
      check=True
      print ("Three of a Kind")
      self.tlist.append(count)
    else:
      self.Check_Two(sort_hand)



  def Check_Two (self, hand):  
    """This function checks if there are two cards of the same rank, and another two of same rank. 
    : e.g. KK993. It returns the count and prints out 'Two Pair' if true, if false, pass down to isOne() """

    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=3
    count=hand*13**5+self.partial_score(sort_hand)
    rank_1=sort_hand[1].rank                        #in a five cards sorted group, if Check_Two(), the 2nd and 4th card should have another identical rank
    rank_2=sort_hand[3].rank
    mylist=[]
    for card in sort_hand:
      mylist.append(card.rank)
    if mylist.count(rank_1)==2 and mylist.count(rank_2)==2:
      check=True
      print ("Two Pair")
      self.tlist.append(count)
    else:
      self.Check_Onepair(sort_hand)



  def Check_Onepair (self, hand):      
    """This function checks if there are two cards of the same rank. 
    : e.g. KKJ23"""                           
    sort_hand=sorted(hand,reverse=True)
    check=True
    hand=2
    total_points=hand*13**5+self.partial_score(sort_hand)
    ranks=[]                                       #create an empty list to store ranks
    EachRankcount=[]                                      #create an empty list to store number of count of each rank
    for card in sort_hand:
      ranks.append(card.rank)
    for each in ranks:
      count=ranks.count(each)
      EachRankcount.append(count)
    if EachRankcount.count(2)==2 and EachRankcount.count(1)==3:  
    #There should be only 2 same numbers and the rest are all different
      check=True
      print ("One Pair")
      self.tlist.append(total_points)
    else:
      self.Check_High(sort_hand)


  def Check_High (self, hand): 
    """This function checks for the highest card in a players' cards."""                        
    sort_hand=sorted(hand,reverse=True)
    hand=1
    count=hand*13**5+self.partial_score(sort_hand)
    mylist=[]                                       #create a list to store ranks
    for card in sort_hand:
      mylist.append(card.rank)
    print ("High Card")
    self.tlist.append(count)


    


  
