#Educative or some other platform
def knapsack(weights, prices, capacity):
  def maxProfit(s, ws, ps, cap, mem = {}):

    if s <= cap:
      return sum(ps)
    if tuple(ws) in mem:
      return mem[tuple(ws)]
    pft = 0
    for idx in range(len(ws)):
      p = maxProfit(s - ws[idx], ws[:idx] + ws[idx+1:], ps[:idx] + ps[idx+1:], cap)
      if p > pft:
        pft = p
    
    mem[tuple(ws)] = pft
    return pft

  return maxProfit(sum(weights), weights, prices, capacity)
