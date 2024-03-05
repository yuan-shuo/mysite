# 第二章建筑设计
class Archi:
    def __init__(
            self, s_l:float, n_l:int,
            qu_b:int, qd_b:int, r_b:float, n_b:int, c_b:float,
            enter:dict,
            div_b=2, m_b=0, k=1.4, w_n=3, tm=4, bn=1.25, ct=3200,
            ab=0.15
            ):

        # i1.站台有效长度数据计算
        #region
        self.delta = 2 # 列车停车误差
        self.s_l = s_l # 列车每节长度
        self.n_l = n_l # 列车节数
        self.l = int(s_l*n_l + self.delta) # 站台有效长度
        #endregion

        # i2.楼梯与自动楼梯
        #region
        self.ability_m = 8100 # 自动扶梯运送能力
        self.ability_n = 3200 # 步行扶梯运送能力
        self.m = int(qd_b * k / (self.ability_m*0.7)) + 2 # 自动扶梯数量
        self.n_width = qu_b * k / (self.ability_n*0.7)
        self.n = int(self.n_width / w_n) + 2 # 步行楼梯数量
        self.w_n = w_n # 步行楼梯宽度
        self.tm = tm # 最大逃生时间
        self.qu_b = qu_b # = (上车人数/h) * k超高峰系数
        self.div_b = div_b
        #endregion

        # i3.站台宽度计算（客流计算法）
        #region
        self.b_a = m_b if m_b else 0.4
        self.b_b1 = round((qu_b * r_b * div_b / (self.l*60) + self.b_a),3)
        self.b_b2 = round(((qu_b + qd_b) * r_b * div_b / (self.l*60) + m_b),3)
        self.b_b = round(max(
            self.b_b1,
            self.b_b2,
            2.5
        ),1)
        self.b = max(2*self.b_b + n_b*c_b + (self.w_n+1), 8)
        #endregion

        # i4.售检票设施数量计算
        #region
        self.hr = 0.5
        self.N1_a = qu_b*self.hr/600
        self.N1_h = qu_b*self.hr/1200
        self.N2_in = qu_b/1200
        self.N2_out = qd_b/1200
        #endregion

        # i5.出入口设计
        #region
        self.enter = {key:(value*k*bn)/ct for key,value in enter.items()}
        self.enter_stair = {key:(value*div_b*(1+ab))/ct for key,value in enter.items()}
        #endregion

    # d1.站台有效长度文本输出(in:len, out:str)
    def len_val(self, len:int = None):
        if not len:
            l = self.l
        else:
            l = len
        text = f"""
                本站过站车辆为{self.n_l}辆编组，
                列车每节长度为{self.s_l}m，
                故本站站台有效长度为{self.n_l}*{self.s_l}+1~2 = {self.n_l*self.s_l+1}~{self.n_l*self.s_l+2}m，
                取为{l}m。
                """
        text = text.replace("\n", "").replace(" ", "")
        self.l = l
        return text
    
    # d2.楼梯与自动楼梯宽度文本及逃生时间检算(in:time + admin + max, out:str*3 + bool)
    def stair_enscape(self, time=None, admin=10, max=310):
        if time:
            t = time
        else:
            t = self.tm
        t_out = round(1 + (
            (self.n_l*max+(self.qu_b*self.div_b/60 + 10))
            /
            (0.9*(8100*(self.m-1)+3700*self.n*self.w_n)/60)
            ),3)
        enscape = t_out < t
        # print(t_out)
        # print(enscape)
        text1 = f"""
                考虑在{self.l}m站台长度内，至少设置2个出站口，
                因此选取{self.m}部1m宽自动扶梯，同时为保证事故疏散时间的要求，
                采用{self.n}部{self.w_n}m宽楼梯。
                """
        text2 = f"""
                人行楼梯和自动扶梯总量布置除应满足上、下乘客的需要外，
                还应按站台层的事故疏散时间不大于{t}min进行验算，
                消防专用梯及垂直电梯不计入事故疏散用。
                """
        text3 = f"""
                计算中，考虑1台自动扶梯损坏不能运行，
                (N-1)台自动扶梯和人行楼梯的通过能力按9折折减，
                式子中“1”为人的反应时间，单位为min；
                T={t_out}min{"<" if enscape else ">"}{t}min，
                {"满足" if enscape else "不满足"}规范防灾要求。
                """
        text1 = text1.replace("\n", "").replace(" ", "")
        text2 = text2.replace("\n", "").replace(" ", "")
        text3 = text3.replace("\n", "").replace(" ", "")
        return text1, text2, text3
        
    # d3.岛式站台宽度计算(in:none, out:str*2)
    def width(self):
        text1 = f"""
                通过两种方式求得的b分别为{self.b_b1}m、{self.b_b2}m，取b={self.b_b}m
                """
        text2 = f"""
                已知b={self.b_b}m，计算岛式站台宽度B={self.b}m，
                考虑到自动扶梯安装宽度及楼梯扶手宽度等，站台宽度取{int(self.b+2)}m。
                """
        self.b = int(self.b + 2)
        text1 = text1.replace("\n", "").replace(" ", "")
        text2 = text2.replace("\n", "").replace(" ", "")
        return text1, text2

    # d4.售检票设施数量计算(in:none, out:str*4)
    def equ(self):
        t1 = f"根据计算，所需自动售票机台数为{round(self.N1_a,1)}台，"
        self.N1_a = int(self.N1_a)+4 if int(self.N1_a)%2==0 else int(self.N1_a)+3
        t2 = f"取{self.N1_a}台，每边各{int(self.N1_a/2)}台。"
        text1 = t1 + t2

        t1 = f"根据计算，所需人工窗口数为{round(self.N1_h,1)}间，"
        self.N1_h = int(self.N1_h)+4 if int(self.N1_h)%2==0 else int(self.N1_h)+3
        t2 = f"由于同时设置了自动售票机，因此设置{self.N1_h}间来满足要求，每边{int(self.N1_h/2)}间。"
        text2 = t1 + t2
        
        t1 = f"根据计算，进站检票机台数为{round(self.N2_in,1)}台，"
        self.N2_in = int(self.N2_in)+4 if int(self.N2_in)%2==0 else int(self.N2_in)+3
        t2 = f"取{self.N2_in}台，每边各{int(self.N2_in/2)}台。"
        t3 = "同时在检票机旁设置一具有一定宽度的人工开启栅栏门以便于处理较大行李出入的问题。"
        text3 = t1 + t2 +t3

        t1 = f"根据计算，出站检票机台数为{round(self.N2_out,1)}台，"
        self.N2_out = int(self.N2_out)+4 if int(self.N2_out)%2==0 else int(self.N2_out)+3
        t2 = f"取{self.N2_out}台，每边各{int(self.N2_out/2)}台。"
        t3 = "出站检票口附近各设一补票亭，以便乘客补票。"
        text4 = t1 + t2 +t3
        return  text1, text2, text3, text4

    # d5.出入口计算(in:none, out:list*2)
    def entrance(self):
        text1 = []
        for key, value in self.enter.items():
            v_old = round(value,1)
            self.enter[key] = max(2.5, round(value,1))
            text1.append(f"根据计算得{key}通道宽度为{v_old}，同时出入口宽度不小于2.5m，取{self.enter[key]}m。")

        text2 = []
        for key, value in self.enter_stair.items():
            v_old = round(value,1)
            tx1 = ""
            if v_old > self.enter[key]:
                self.enter[key] = v_old
                tx1 = f"，由于楼梯宽度大于对应通道宽度，按楼梯宽度计算"
            else:
                self.enter_stair[key] = max(2.5, self.enter[key])

            text2.append(f"根据计算得{key}通道楼梯宽度为{v_old}" +tx1+ f"，取{self.enter_stair[key]}m。")

        return text1, text2

if __name__ == "__main__":
    archi = Archi(
        s_l=22.8, n_l=4,
        qu_b=1950, qd_b=1934, r_b=0.5, n_b=2, c_b=0.7,
        enter={
            "A1":810,
            "A2":810,
            "B1":448,
            "B2":471,
            "C":938
        }
        )
    # print(archi.l)
    # print(archi.b_b)
    # print(archi.m)
    # print(archi.n_width)
    # print(archi.n)
    # print(enscape)
    # print(archi.enter)

    t1 = archi.len_val()
    # print(f"a.{t1}")
    # t1, t2, t3, enscape = archi.stair_enscape()
    # print(f"b.{t1}\nc.{t2}\nd.{t3}")
    # print(archi.b)
    # t1, t2 = archi.width()
    # print(f"e.{t1}\nf.{t2}")
    # t1, t2, t3, t4 = archi.equ()
    # print(f"g.{t1}\ng.{t2}\ni.{t3}\nj.{t4}")
    
    t1, t2 = archi.entrance()
    print(t1, t2)