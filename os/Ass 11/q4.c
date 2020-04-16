/* Eisenberg-McGuire algorithm: a software approach to N-process
   mutual exclusion.

   For description of Eisenberg-McGuire algorithm, see page 261 of
   "Concurrent Systems - Operating Systems, Database and Distributed
   Systems: An Inegrated Approach / Jean Bacon -- 2nd Edition".

   Copyrigh (c) 2001 Xiao Zhang */

#include <stdlib.h>
#include <pthread.h>
#include <iostream>
/**********************************************************************/
/* Eisenberg-McGuire's algorithm for N-process mutual exclusion       */
/**********************************************************************/

class eis_mcg_mutex_t {

 private:

  int n;
  enum procphase { out_cr, want_cr, claim_cr } *procphase;
  int turn;

 public:

  /* Initialize the mutex data shared by N processes */

  eis_mcg_mutex_t(int nproc) {
    n = nproc;
    procphase = new enum procphase [n];
    srand(time(0));
    turn = (int) (1.0 * n * rand() / (RAND_MAX + 1.0));
    for (int i = 0; i < n; i++) procphase[i] = out_cr;
  }

  ~eis_mcg_mutex_t() {
    delete [] procphase;
  }

  /* Entry protocol for process i */

  void mutex_lock(int i) {
    procphase[i] = want_cr;
    int j = turn;
    do {
      while (j != i) {
	if (procphase[j] == out_cr) j = (j + 1) % n;
	else j = turn;
      }
      procphase[i] = claim_cr;
      j = (j + 1) % n;
      while (procphase[j] != claim_cr) j = (j + 1) % n;
    } while (!(j == i && (turn == i || procphase[turn] == out_cr)));
    turn = i;
  }

  /* Exit protocol for process i */

  void mutex_unlock(int i) {
    int j = (turn + 1) % n;
    while (procphase[j] == out_cr) j = (j + 1) % n;
    turn = j;
    procphase[i] = out_cr;
  }

};

/**********************************************************************/
/* To test the Eisenberg-McGuire's algorithm, we write a simple       */
/* program that creates N threads (processes) and then has each       */
/* thread increment a global variable `counter' NLOOP times. The      */
/* final value of `counter' is expected to be N * NLOOP.              */
/**********************************************************************/

#define N	4		/* number of threads */
#define NLOOP	1000		/* number of times each thread loops */

int counter;			/* this is cremented by the threads */
eis_mcg_mutex_t counter_in_use(N);

void *doit(void *arg)
{
  int i, val;
  int tid = (int)arg;

  /* Each thread fetches, prints and increments the counter NLOOP times.
     The value of the counter should increase monotonically. */

  for (i = 0; i < NLOOP; i++) {

    /* Replace pthread_mutex_lock() with Eisenberg-McGuire's
       enter-critical-section procedure. */
    counter_in_use.mutex_lock(tid);
    
    /* Here is critical section */
    val = counter;
    counter = val + 1;
    cout << tid << ": " << counter << endl;

    /* Replace pthread_mutex_unlock() with Eisenberg-McGuire's
       leave-critical-section procedure. */
    counter_in_use.mutex_unlock(tid);

  }

  return NULL;
}

int main()
{
  pthread_t tid[N];
  int i;

  for (i = 0; i < N; i++) pthread_create(&tid[i], NULL, doit, (void *)i);
  for (i = 0; i < N; i++) pthread_join(tid[i], NULL);

  return 0;
}
