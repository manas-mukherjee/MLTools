from concurrent import futures

from src.tutorials.fluentpython.concurrency_futures.Standardflags import get_flag, show, save_flag, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

def download_many_without_exec(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)

if __name__ == '__main__':
    main(download_many_without_exec)


# As of Python 3.4, there are two classes named Future in the standard library: concurrent.futures.Future and asyncio.Future
# both Future classes have an .add_done_callback() method: you give it a callable,
    # and the callable will be invoked with the future as the single argument when the future is done.

# Not truly parallel. Restricted by - Global Interpreter Lock (GIL)

# However, all standard library functions that perform blocking I/O release the GIL when waiting for a result from the OS.
# This means Python programs that are I/O bound can benefit from using threads at the Python level:
# while one Python thread is waiting for a response from the network, the blocked I/O function releases the GIL so another thread can run.


