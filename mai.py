from safety_rules import check_helmet, check_vest

def site_safety_check(worker_name, helmet, vest):
    print(f"Checking safety for {worker_name}...")

    if check_helmet(helmet) and check_vest(vest):
        print("Status: SAFE ✅")
    else:
        print("Status: NOT SAFE ❌")

if __name__ == "__main__":
    site_safety_check("Worker 1", helmet=True, vest=False)
