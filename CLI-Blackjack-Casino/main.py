import random
import time
import os
suits = ["Sekop ♠", "Hati ♥", "Keriting ♣", "Wajik ♦"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9, "10": 10, "J": 10,"Q": 10,"K": 10,"A": 11}
money = 10000
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
def buat_deck():
  """Membuat satu set kartu baru dan mengacaknya."""
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append({"suit": suit, "rank": rank, "value": values[rank]})
  random.shuffle(deck)
  return deck
def hitung_total(hand):
  total = sum(card["value"] for card in hand)
  jumlah_as = sum(1 for card in hand if card["rank"] == "A")
  while total > 21 and jumlah_as > 0:
    total -= 10
    jumlah_as -= 1
  return total
def tampilkan_kartu(hand, sembunyikan_pertama=False):
  kartu_str = []
  if sembunyikan_pertama:
    kartu_str.append("[???]")
    kartu_str.extend([f"[{k['rank']} {k['suit']}]" for k in hand[1:]])
  else:
    kartu_str = [f"[{k['rank']} {k['suit']}]" for k in hand]
  return " ".join(kartu_str)
def play_hand(deck, hand, bet, current_money):
  if hitung_total(hand) == 21:
    print(f"Kartu: {tampilkan_kartu(hand)} | Total: 21")
    print("BLACKJACK!")
    return hitung_total(hand), bet * 2.5, True
  playing = True
  first_turn = True
  while playing:
    total = hitung_total(hand)
    print(f"\nKartu Anda: {tampilkan_kartu(hand)}")
    print(f"Total Nilai: {total}")
    if total > 21:
      print("BUST! Anda melebih 21.")
      return total, 0, False 
    if total == 21:
      print("Poin Maksimal 21!")
      return total, bet, False
    options = "[H]it  [S]tand"
    if first_turn and current_money >= bet:
      options += "  [D]ouble"
    print(f"Opsi: {options}")
    choice = input("Pilihan Anda: ").lower()
    if choice == 'h':
      print("Mengambil kartu...")
      time.sleep(1)
      hand.append(deck.pop())
      first_turn = False 
    elif choice == 's':
      print("Anda memilih Stand.")
      playing = False
    elif choice == 'd' and first_turn and current_money >= bet:
      print("DOUBLE DOWN! Taruhan digandakan, ambil 1 kartu terakhir.")
      current_money -= bet  
      bet *= 2
      time.sleep(1)
      hand.append(deck.pop())
      print(
          f"Kartu Akhir: {tampilkan_kartu(hand)} (Total: {hitung_total(hand)})")
      playing = False  
      return hitung_total(hand), bet, False
    else:
      print("Input tidak valid atau uang tidak cukup untuk Double.")
  return hitung_total(hand), bet, False

def game_loop():
  global money
  clear_screen()
  print("=================================")
  print("   SELAMAT DATANG DI BLACKJACK  ")
  print("=================================")
  while True:
    if money <= 0:
      print("Anda bangkrut! Game Over.")
      break
    print(f"\nUang Anda: ${money}")
    try:
      bet_input = input("Masukkan taruhan (0 untuk keluar): $")
      if not bet_input.isdigit(): continue
      bet = int(bet_input)
    except ValueError:
      continue
    if bet == 0:
      print("Terima kasih telah bermain!")
      break
    if bet > money:
      print("Uang tidak cukup!")
      continue
    money -= bet
    deck = buat_deck()
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    print("\n--- DEALER ---")
    print(f"Kartu: {tampilkan_kartu(dealer_hand, sembunyikan_pertama=True)}")
    active_hands = []
    if player_hand[0]['value'] == player_hand[1]['value'] and money >= bet:
      print(f"\nKartu Anda: {tampilkan_kartu(player_hand)}")
      ask_split = input(
          "Anda mendapat kartu kembar! Mau SPLIT? (y/n): ").lower()
      if ask_split == 'y':
        money -= bet
        print("Melakukan Split...")
        hand1 = [player_hand[0], deck.pop()]
        hand2 = [player_hand[1], deck.pop()]
        active_hands.append({'hand': hand1, 'bet': bet, 'status': 'playing'})
        active_hands.append({'hand': hand2, 'bet': bet, 'status': 'playing'})
      else:
        active_hands.append({'hand': player_hand,'bet': bet,'status': 'playing'})
    else:
      active_hands.append({'hand': player_hand,'bet': bet,'status': 'playing'})
    final_results = []
    for i, item in enumerate(active_hands):
      if len(active_hands) > 1:
        print(f"\n--- Memainkan Tangan ke-{i+1} ---")
      score, final_bet, is_bj = play_hand(deck, item['hand'], item['bet'],money)
      if final_bet > item['bet'] and not is_bj:
        money -= (final_bet - item['bet'])
      final_results.append({'score': score,'bet': final_bet,'blackjack': is_bj})
    all_busted = all(res['score'] > 21 for res in final_results)
    if not all_busted:
      print("\n--- GILIRAN DEALER ---")
      time.sleep(1)
      print(f"Dealer membuka kartu: {tampilkan_kartu(dealer_hand)}")
      dealer_score = hitung_total(dealer_hand)
      while dealer_score < 17:
        print("Dealer mengambil kartu (Hit)...")
        time.sleep(1)
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print(f"Dealer dpt: {new_card['rank']} {new_card['suit']}")
        dealer_score = hitung_total(dealer_hand)
      print(f"Total Dealer: {dealer_score}")
    else:
      dealer_score = hitung_total(dealer_hand) 
    print("\n--- HASIL AKHIR ---")
    for i, res in enumerate(final_results):
      p_score = res['score']
      p_bet = res['bet']
      p_bj = res['blackjack']
      prefix = f"Tangan {i+1}: " if len(active_hands) > 1 else ""
      if p_bj:
        print(f"{prefix}Blackjack! Anda Menang ${p_bet}")
        money += p_bet 
      elif p_score > 21:
        print(f"{prefix}Bust ({p_score}). Anda Kalah ${p_bet}")
      elif dealer_score > 21:
        print(f"{prefix}Dealer Bust! Anda Menang! (+${p_bet})")
        money += (p_bet * 2)  
      elif p_score > dealer_score:
        print(f"{prefix}Anda ({p_score}) vs Dealer ({dealer_score}). Anda Menang! (+${p_bet})")
        money += (p_bet * 2)
      elif p_score < dealer_score:
        print(f"{prefix}Anda ({p_score}) vs Dealer ({dealer_score}). Dealer Menang.")
      else:
        print(f"{prefix}Push/Seri ({p_score} vs {dealer_score}). Uang kembali.")
        money += p_bet
    time.sleep(2)
if __name__ == "__main__":
  game_loop()
