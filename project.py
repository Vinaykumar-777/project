import random

def ask_question(level, question, answers, hints, full_score, hint_score, penalty):
    hint_count = 0
    attempts = 0
    
    print(f"\n🔶 LEVEL {level}")
    
    while True:
        ans = input(question).lower()
        attempts += 1
        
        if ans == "hint":
            if hint_count < 3:
                print(f"💡 Hint {hint_count + 1}: {hints[hint_count]}")
                hint_count += 1
            else:
                print("❗ No more hints!")
        
        elif any(a in ans for a in answers):
            print("✅ Correct!")
            return hint_score if hint_count > 0 else full_score
        
        else:
            print("❌ Wrong!")
        
        if hint_count >= 3 and attempts >= 5:
            print("➡️ Moving forward with penalty!")
            return -penalty


# Game start
score = 0
print("🏃‍♂️ PATH TO FREEDOM - 10 LEVEL CHALLENGE")
print("Solve each level to reach the goal!")
print("Type 'hint' for help (max 3 per level)\n")

# LEVEL 1 (Very Easy)
score += ask_question(1,
"I speak without a mouth and hear without ears. What am I?\n",
["echo"],
["Repeats sound", "Heard in caves", "Voice reflection"],
10, 5, 2)

# LEVEL 2
score += ask_question(2,
"2, 4, 8, 16, ?\n",
["32"],
["Doubling", "×2 pattern", "16×2"],
15, 8, 3)

# LEVEL 3
score += ask_question(3,
"The more you take, the more you leave behind?\n",
["footsteps","steps"],
["Walking related", "Leaves behind", "Movement"],
20, 10, 5)

# LEVEL 4
score += ask_question(4,
"5 + 3 × 2 = ?\n",
["11"],
["BODMAS", "Multiply first", "3×2=6"],
25, 12, 5)

# LEVEL 5
score += ask_question(5,
"I have keys but no locks. What am I?\n",
["keyboard"],
["Computer", "Typing", "Keys"],
30, 15, 7)

# LEVEL 6 (Medium-Hard)
score += ask_question(6,
"12 ÷ 4 + 6 × 2 = ?\n",
["15"],
["Division first", "Then multiply", "3 + 12"],
35, 18, 8)

# LEVEL 7
score += ask_question(7,
"I am tall when young, short when old. What am I?\n",
["candle"],
["Melts", "Fire", "Wax"],
40, 20, 10)

# LEVEL 8 (Hard)
score += ask_question(8,
"Find missing: 3, 9, 27, ?, 243\n",
["81"],
["×3 pattern", "27×3", "Middle number"],
45, 22, 12)

# LEVEL 9 (Very Hard)
score += ask_question(9,
"If 2+3=10, 3+4=21, then 4+5=?\n",
["36"],
["Pattern trick", "(a+b)*a", "9×4"],
50, 25, 15)

# LEVEL 10 (Final Boss 🔥)
score += ask_question(10,
"I can fly without wings, cry without eyes. What am I?\n",
["cloud"],
["Sky", "Rain", "No wings"],
60, 30, 20)

# FINAL RESULT
print("\n🏁 FINAL RESULT")
print("Your Score:", score)

if score >= 250:
    print("🏆 MASTER ESCAPE! (Excellent)")
elif score >= 150:
    print("🎉 SUCCESS! You reached the goal!")
else:
    print("⚠️ You reached, but need improvement!")