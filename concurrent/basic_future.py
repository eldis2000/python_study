import time
import concurrent.futures

def worker(index):
    print("worker index : %s" % index)
    time.sleep(index)
    return ("Complete %s worker job" % index)

def main():
    future_list = []
    executer = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    ################################################################
    #not works in android tumux platform
    #https://github.com/termux/termux-packages/issues/570
    ################################################################
    #executer = concurrent.futures.ProcessPoolExecutor(max_workers=3)

    for i in range(5):
        future = executer.submit(worker, i)
        future_list.append(future)

    time.sleep(1)

    for idx, future in enumerate(future_list):
        if future.done():
            print("result : %s" % future.result())
            continue

        print("[%s worker] Wait for 1 second because it has not finished yet." % idx)

        try:
            result = future.result(timeout=1)
        except concurrent.futures.TimeoutError:
            print("[%s worker] Timeout error" % idx)
        else:
            print("result : %s" % result)

    executer.shutdown(wait=False)

if __name__ == "__main__":
    main()
