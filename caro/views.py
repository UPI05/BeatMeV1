from django.shortcuts import render
from caro.models import botInfo, alertDt
from django.http import HttpResponse, JsonResponse
import random as rd
# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'botDt': botInfo.objects.all(), 'alertDt': alertDt.objects.all()})
def handle404(request, exception = None):
    return render(request, 'pages/404.html', status=404)
def handle500(request, exception = None):
    return render(request, 'pages/500.html', status=500)
    

stat = []
MAX, MIN = 10000, -10000
def check4(deny, k, ch, st):
    op = 2
    if ch == 2: op = 1
    num = 0
    for i in range(1, 20):
        for j in range(1, 20):
            if j + 3 > 19: continue
            if st[i][j] == op or st[i][j + 1] == op or st[i][j + 2] == op or st[i][j + 3] == op: continue
            cnt = 0
            if st[i][j] == ch: cnt+=1
            if st[i][j + 1] == ch: cnt+=1
            if st[i][j + 2] == ch: cnt+=1
            if st[i][j + 3] == ch: cnt+=1
            if cnt >= k:
                left = j + 3
                if st[i][j + 2] == ch: left = j + 2
                if st[i][j + 1] == ch: left = j + 1
                if st[i][j] == ch: left = j
                right = j
                if st[i][j + 1] == ch: right = j + 1
                if st[i][j + 2] == ch: right = j + 2
                if st[i][j + 3] == ch: right = j + 3
                cnt = 0
                for x in range(right + 1, 20):
                    if st[i][x] != op: cnt+=1
                    break
                for x in range(left - 1, 0, -1):
                    if st[i][x] != op: cnt+=1
                    break
                if deny:
                    if cnt == 1: num+=1
                else:
                    if cnt == 2: num+=1
    for i in range(1, 20):
        for j in range(1, 20):
            if i + 3 > 19: continue
            if st[i][j] == op or st[i + 1][j] == op or st[i + 2][j] == op or st[i + 3][j] == op: continue
            cnt = 0
            if st[i][j] == ch: cnt+=1
            if st[i + 1][j] == ch: cnt+=1
            if st[i + 2][j] == ch: cnt+=1
            if st[i + 3][j] == ch: cnt+=1
            if cnt >= k:
                left = i + 3
                if st[i + 2][j] == ch: left = i + 2
                if st[i + 1][j] == ch: left = i + 1
                if st[i][j] == ch: left = i
                right = i
                if st[i + 1][j] == ch: right = i + 1
                if st[i + 2][j] == ch: right = i + 2
                if st[i + 3][j] == ch: right = i + 3
                cnt = 0
                for x in range(right + 1, 20):
                    if st[x][j] != op: cnt+=1
                    break
                for x in range(left -1, 0, -1):
                    if st[x][j] != op: cnt+=1
                    break
                if deny:
                    if cnt == 1: num+=1
                else:
                    if cnt == 2: num+=1
    for i in range(1, 20):
        for j in range(1, 20):
            if j + 3 > 19 or i + 3 > 19: continue
            if st[i][j] == op or st[i + 1][j + 1] == op or st[i + 2][j + 2] == op or st[i + 3][j + 3] == op: continue
            cnt = 0
            if st[i][j] == ch: cnt+=1
            if st[i + 1][j + 1] == ch: cnt+=1
            if st[i + 2][j + 2] == ch: cnt+=1
            if st[i + 3][j + 3] == ch: cnt+=1
            if cnt >= k:
                left = i + 3
                left2 = j + 3
                if st[i + 2][j + 2] == ch:
                    left = i + 2
                    left2 = j + 2
                if st[i + 1][j + 1] == ch:
                    left = i + 1
                    left2 = j + 1
                if st[i][j] == ch:
                    left = i
                    left2 = j
                right = i
                right2 = j
                if st[i + 1][j + 1] == ch: 
                    right = i + 1
                    right2 = j + 1
                if st[i + 2][j + 2] == ch: 
                    right = i + 2
                    right2 = j + 2
                if st[i + 3][j + 3] == ch: 
                    right = i + 3
                    right2 = j + 3
                cnt = 0
                if ((right + 1) <= 19 and (right2 + 1) <= 19):
                    if st[right + 1][right2 + 1] != op: cnt+=1
                if ((left - 1) >= 1 and (left2 - 1) >= 1):
                    if st[left - 1][left2 - 1] != op: cnt+=1
                if deny:
                    if cnt == 1: num+=1
                else:
                    if cnt == 2: num+=1
    for i in range(1, 20):
        for j in range(1, 20):
            if j - 3 < 1 or i + 3 > 19: continue
            if st[i][j] == op or st[i + 1][j - 1] == op or st[i + 2][j - 2] == op or st[i + 3][j - 3] == op: continue
            cnt = 0
            if st[i][j] == ch: cnt+=1
            if st[i + 1][j - 1] == ch: cnt+=1
            if st[i + 2][j - 2] == ch: cnt+=1
            if st[i + 3][j - 3] == ch: cnt+=1
            if cnt >= k:
                left = i + 3
                left2 = j - 3
                if st[i + 2][j - 2] == ch:
                    left = i + 2
                    left2 = j - 2
                if st[i + 1][j - 1] == ch:
                    left = i + 1
                    left2 = j - 1
                if st[i][j] == ch:
                    left = i
                    left2 = j
                right = i
                right2 = j
                if st[i + 1][j - 1] == ch: 
                    right = i + 1
                    right2 = j - 1
                if st[i + 2][j - 2] == ch: 
                    right = i + 2
                    right2 = j - 2
                if st[i + 3][j - 3] == ch: 
                    right = i + 3
                    right2 = j - 3
                cnt = 0
                if ((right + 1) <= 19 and (right2 - 1) >= 1):
                    if st[right + 1][right2 - 1] != op: cnt+=1
                if ((left - 1) <= 19 and (left2 + 1) >= 1):
                    if st[left - 1][left2 + 1] != op: cnt+=1
                if deny:
                    if cnt == 1: num+=1
                else:
                    if cnt == 2: num+=1
    return num
def evaluate(x, y, st):
    ans = 0
    if check4(False, 4, 1, st) >= 3: ans = -1000
    elif check4(False, 4, 1, st) >= 2: ans = -980
    elif check4(False, 4, 1, st) >= 1: ans = -960
    elif check4(True, 4, 3, st) >= 3: ans = -800
    elif check4(True, 4, 1, st) >= 2: ans = -780
    elif check4(True, 4, 1, st) >= 1: ans = -760
    elif check4(False, 4, 2, st) >= 3: ans = 1000
    elif check4(False, 4, 2, st) >= 2: ans = 980
    elif check4(False, 4, 2, st) >= 1: ans = 960
    elif check4(True, 4, 2, st) >= 3: ans = 800
    elif check4(True, 4, 2, st) >= 2: ans = 780
    elif check4(True, 4, 2, st) >= 1: ans = 760
    elif check4(False, 3, 1, st) >= 3: ans = -600
    elif check4(False, 3, 1, st) >= 2: ans = -580
    elif check4(False, 3, 1, st) >= 1: ans = -560
    elif check4(True, 3, 1, st) >= 3: ans = -400
    elif check4(True, 3, 1, st) >= 2: ans = -380
    elif check4(True, 3, 1, st) >= 1: ans = -360
    elif check4(False, 3, 2, st) >= 3: ans = 600
    elif check4(False, 3, 2, st) >= 2: ans = 580
    elif check4(False, 3, 2, st) >= 1: ans = 560
    elif check4(True, 3, 2, st) >= 3: ans = 400
    elif check4(True, 3, 2, st) >= 2: ans = 380
    elif check4(True, 3, 2, st) >= 1: ans = 360
    elif check4(False, 2, 1, st) >= 3: ans = -200
    elif check4(False, 2, 1, st) >= 2: ans = -180
    elif check4(False, 2, 1, st) >= 1: ans = -160
    elif check4(True, 2, 1, st) >= 3: ans = -100
    elif check4(True, 2, 1, st) >= 2: ans = -80
    elif check4(True, 2, 1, st) >= 1: ans = -60
    elif check4(False, 2, 2, st) >= 3: ans = 200
    elif check4(False, 2, 2, st) >= 2: ans = 180
    elif check4(False, 2, 2, st) >= 1: ans = 160
    elif check4(True, 2, 2, st) >= 3: ans = 100
    elif check4(True, 2, 2, st) >= 2: ans = 80
    elif check4(True, 2, 2, st) >= 1: ans = 60
    elif check4(False, 1, 1, st) >= 3: ans = -40
    elif check4(False, 1, 1, st) >= 2: ans = -20
    elif check4(False, 1, 1, st) >= 1: ans = -10
    elif check4(True, 1, 1, st) >= 3: ans = -8
    elif check4(True, 1, 1, st) >= 2: ans = -6
    elif check4(True, 1, 1, st) >= 1: ans = -4
    elif check4(False, 1, 2, st) >= 3: ans = 40
    elif check4(False, 1, 2, st) >= 2: ans = 20
    elif check4(False, 1, 2, st) >= 1: ans = 10
    elif check4(True, 1, 2, st) >= 3: ans = 8
    elif check4(True, 1, 2, st) >= 2: ans = 6
    elif check4(True, 1, 2, st) >= 1: ans = 4
    return [ans, x, y]

def minimax(depth, x, y, sta, maximizingPlayer, alpha, beta):
    if checkResult(2, 5, sta): return [2000, x, y]
    if checkResult(1, 5, sta): return [-2000, x, y]
    if depth == 0:
        return evaluate(x, y, sta)
    if maximizingPlayer:
        best = MIN
        x, y = 0, 0
        ok = True
        for i in range(1, 20):
            if ok == False: break
            for j in range(1, 20):
                if sta[i][j]: continue
                sta[i][j] = 2
                val = minimax(depth + 1, i, j, sta.copy(), False, alpha, beta)
                if val[0] > best:
                    best = val[0]
                    x = val[1]
                    y = val[2]
                alpha = max(alpha, best)
                sta[i][j] = 0
                if beta <= alpha:
                    ok = False
                    break
        return [best, x, y]
    else:
        best = MAX
        x, y = 0, 0
        ok = True
        for i in range(1, 20):
            if ok == False: break
            for j in range(1, 20):
                if sta[i][j]: continue
                sta[i][j] = 1
                val = minimax(depth + 1, i, j, sta.copy(), True, alpha, beta)
                if val[0] < best:
                    best = val[0]
                    x = val[1]
                    y = val[2]
                beta = min(beta, best)
                sta[i][j] = 0
                if beta <= alpha:
                    ok = False
                    break
        return [best, x, y]

def findWay(x, y):
    maxVal = -100000
    store = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    for i in range(1, 20):
        for j in range(1, 20):
            if stat[i][j]: continue
            stat[i][j] = 2
            res = minimax(0, i, j, stat.copy(), False, MIN, MAX)
            store[i][j] = res[0]
            if res[0] > maxVal:
                maxVal = res[0]
            stat[i][j] = 0
    ans = []
    for i in range(1, 20):
        for j in range(1, 20):
            if store[i][j] == maxVal:
                ans.append([i, j])
    x = rd.randint(0, len(ans) - 1)
    a = ans[x][0]
    b = ans[x][1]
    stat[a][b] = 2
    return [a, b]

def checkResult(ch, k, st):
    for i in range(1, 20):
        for j in range(1, 20):
            if st[i][j] != ch:
                continue
            if i + k - 1 <= 19:
                ok = True;
                for x in range(1, k):
                    if st[i][j] != st[i + x][j]:
                        ok = False
                        break
                if ok: return ok
            if j + k - 1 <= 19:
                ok = True;
                for x in range(1, k):
                    if st[i][j] != st[i][j + x]:
                        ok = False
                        break
                if ok: return ok
            if (i + k - 1<= 19) and (j + 4 <= 19):
                ok = True;
                for x in range(1, k):
                    if st[i][j] != st[i + x][j + x]:
                        ok = False
                        break
                if ok: return ok
            if (i + k - 1 <= 19) and (j - 4 >= 1):
                ok = True;
                for x in range(1, k):
                    if st[i][j] != st[i + x][j - x]:
                        ok = False
                        break
                if ok: return ok
    return False

def getMove(request):
    if request.method == 'GET':
        x = int(request.GET['raw'])
        y = int(request.GET['col'])
        stat.clear()
        for i in range(20):
            stat.append(request.GET.getlist(f'dt[{i}][]'))
        for i in range(20):
            for j in range(20):
                stat[i][j] = int(stat[i][j])
        if checkResult(1, 5, stat):
            data = botInfo.objects.get(id = 1)
            data.lose += 1;
            data.save()
            return JsonResponse({'x': 0, 'y': 0}, status = 200)
        ans = findWay(x, y)
        if checkResult(2, 5, stat):
            data = botInfo.objects.get(id = 1)
            data.win += 1;
            data.save()
        return JsonResponse({'x': ans[0], 'y': ans[1]}, status = 200)
    else:
        return JsonResponse({'x': 'Something wrong!', 'y': 'Something wrong!'}, status = 400)