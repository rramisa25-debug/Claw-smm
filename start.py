import multiprocessing
import smm_bot_Final
import Claw_VIP_Final

def run_smm():
    smm_bot_Final.main()

def run_claw():
    Claw_VIP_Final.main()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_smm,  name="SMM_Bot")
    p2 = multiprocessing.Process(target=run_claw, name="Claw_VIP_Bot")

    p1.start()
    p2.start()

    print("✅ SMM Bot চালু!")
    print("✅ Claw VIP Bot চালু!")

    p1.join()
    p2.join()
