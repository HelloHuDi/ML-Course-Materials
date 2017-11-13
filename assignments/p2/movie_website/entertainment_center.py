#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from media import Movie
import fresh_tomatoes

my_movie_1 = Movie("功守道",
                   "通过影片向中国功夫做过贡献的前辈致敬，同时与全世界分享中国文化",
                   "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign="
                   "b3f364854190f60310bd9415587bd87e/4d086e061d950a7b3b79a67001d162d9f2d3c932.jpg",
                   "http://v.youku.com/v_show/id_XMzE0ODM1ODg1Ng==.html?spm=a2hww.20027244.m_250379.5~1~3~A",
                   "马云、李连杰、甄子丹、吴京托尼·贾")
my_movie_2 = Movie("大军师司马懿之虎啸龙吟",
                   "从司马懿戎装佩剑意气风发，到诸葛亮手持白鹤羽扇挥斥方遒，都预示着一场场对战呼之欲出",
                   "http://p3.pstatp.com/origin/2ec100044da088981c31",
                   "http://v.youku.com/v_show/id_XMzAyMDAzNDIxNg==.html?spm=a2h1n.8261147.showInfo.5!2~5~5~5~A",
                   "吴秀波、刘涛、王洛勇")
my_movie_3 = Movie("海上牧云记",
                   "九州大陆正值端朝末年，人类皇族牧云家的六皇子牧云笙、大将军之子穆如寒江、\
                   瀚州八部落的后人硕风和叶之间家国情仇、争夺天下的传奇故事",
                   "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign="
                   "6cb2578f3112b31bd361c57be7715d1f/03087bf40ad162d9edeca9d419dfa9ec8b13cdfc.jpg",
                   "http://v.youku.com/v_show/id_XMzE0Njc4NDk2NA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1",
                   "黄轩、窦骁、周一围、徐璐")
my_movie_4 = Movie("正义联盟",
                   "面对一个全新的世界威胁，超人、蝙蝠侠、神奇女侠、\
                   闪电侠、海王和钢骨六位英雄聚首，与这股未知的威胁对抗",
                   "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2221361200,1898908769&fm=27&gp=0.jpg",
                   "http://video.mtime.com/68349/?mid=70233",
                   "本·阿弗莱克、亨利·卡维尔、盖尔·加朵")
my_movie_5 = Movie("引爆者",
                   "影片讲述了段奕宏饰演的男主角赵旭东，无辜被卷入多派\
                   势力的利益争夺中，化身孤胆英雄自我救赎的故事",
                   "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2470729963,2366566132&fm=11&gp=0.jpg",
                   "http://video.mtime.com/68364/?mid=237204",
                   "段奕宏、余男")
fresh_tomatoes.open_movies_page([my_movie_1, my_movie_2, my_movie_3, my_movie_4, my_movie_5])
