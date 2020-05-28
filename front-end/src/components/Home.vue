<template>
  <div>
<!--    返回顶部-->
    <el-backtop>
      <div
        style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: #1989fa;
      }"
      >
        UP
      </div>
    </el-backtop>
  <el-container class="home-container">
<!--    头部-->
    <el-header>
<!--      logo图片-->
      <div class="image-header">
        <img src="../assets/anyknew-b.png" alt="" class="logo_pic">
        <span class="wenzi-header">全球领先的热点导航网站</span>
      </div>
<!--      logo文字-->
<!--      时间选择器-->
      <div class="block">
        <span class="demonstration"></span>
        <el-date-picker
          class = "time-select"
          v-model="cur_time"
          type="datetime"
          format = "yyyy-MM-dd HH:mm:ss"
          value-format = "yyyy-MM-dd HH:mm:ss"
          placeholder="选择日期时间"
          align="right"
          :picker-options="pickerOptions">
        </el-date-picker>
      </div>
<!--      搜索-->
<!--      <el-button class="searchButton" type="primary" icon="el-icon-search" @click="getSearch">搜索</el-button>-->
<!--      退出按钮-->
      <el-button class="logOutButton" type="info" @click="logout">退出</el-button>
    </el-header>
<!--    主题内容-->
    <el-main>
<!--      综合模块-->
      <div class="zonghe">
<!--        头部-->
        <div class="items_header">
          <span class="big_title">综合</span>
          <el-button type="primary" v-if="this.zonghe_data==='展开分类'" class="showAll" icon="el-icon-bottom" @click="show_zonghe">{{zonghe_data}}</el-button>
          <el-button type="primary" v-else class="showAll" icon="el-icon-arrow-up" @click="show_zonghe">{{zonghe_data}}</el-button>
        </div>
<!--        每行-->
        <div class="items_row">
<!--百度-->
          <div v-if="baidu_xianshi" class="grid-content" @click="show_baidu">
            <img src="../assets/logo/baidu.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/baidu.png" class="small_logo">
              <span class="category">热点</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.baidu" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.baidu.com" class="link">
                <span>百度</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_baidu"></el-button>
            </div>
          </div>
<!--微博-->
          <div v-if="weibo_xianshi" class="grid-content" @click="show_weibo">
            <img src="../assets/logo/weibo.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/weibo.png" class="small_logo">
              <span class="category">热榜</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.weibo" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.weibo.com" class="link">
                <span>微博</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_weibo"></el-button>
            </div>
          </div>
<!--知乎-->
          <div v-if="zhihu_xianshi" class="grid-content" @click="show_zhihu">
            <img src="../assets/logo/zhihu.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/zhihu.png" class="small_logo">
              <span class="category">热榜</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.zhihu" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.zhihu.com" class="link">
                <span>知乎</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_zhihu"></el-button>
            </div>
          </div>
        </div>
        <div class="items_row">
<!--网易-->
        <div v-if="wangyi_xianshi" class="grid-content" @click="show_wangyi">
          <img src="../assets/logo/wangyi.png" class="logos">
        </div>
        <div v-else class="details">
          <div class="tw-header">
            <img src="../assets/logo/wangyi.png" class="small_logo">
            <span class="category">国际</span>
          </div>
          <div class="tw-main">
            <div class="singles" v-for="item in this.wangyi" :key='item'>
              <a class="new" v-if="item.rank<4">
                <div class="single">
                  <span class="seq_highlight">{{item.rank}}</span>
                  <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                  <span class="more">{{item.more}}</span>
                </div>
              </a>
              <a class="new" v-else>
                <div class="single">
                  <span class="seq">{{item.rank}}</span>
                  <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                  <span class="more">{{item.more}}</span>
                </div>
              </a>
            </div>
          </div>
          <div class="tw-footer">
            <a href="https://www.163.com/" class="link">
              <span>网易</span>
            </a>
            <el-button icon="el-icon-arrow-up" mini circle @click="show_wangyi"></el-button>
          </div>
        </div>
<!--qdaily-->
      <div v-if="qdaily_xianshi" class="grid-content" @click="show_qdaily">
        <img src="../assets/logo/qdaily.png" class="logos">
      </div>
      <div v-else class="details">
        <div class="tw-header">
          <img src="../assets/logo/qdaily.png" class="small_logo">
          <span class="category">Top50</span>
        </div>
        <div class="tw-main">
          <div class="singles" v-for="item in this.qdaily" :key='item'>
            <a class="new" v-if="item.rank<4">
              <div class="single">
                <span class="seq_highlight">{{item.rank}}</span>
                <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                <span class="more">{{item.more}}</span>
              </div>
            </a>
            <a class="new" v-else>
              <div class="single">
                <span class="seq">{{item.rank}}</span>
                <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                <span class="more">{{item.more}}</span>
              </div>
            </a>
          </div>
        </div>
        <div class="tw-footer">
          <a href="https://www.qdaily.com/" class="link">
            <span>好奇心日报</span>
          </a>
          <el-button icon="el-icon-arrow-up" mini circle @click="show_qdaily"></el-button>
        </div>
      </div>
<!--头条-->
      <div v-if="toutiao_xianshi" class="grid-content" @click="show_toutiao">
        <img src="../assets/logo/toutiao.png" class="logos">
      </div>
      <div v-else class="details">
        <div class="tw-header">
          <img src="../assets/logo/toutiao.png" class="small_logo">
          <span class="category">热搜</span>
        </div>
        <div class="tw-main">
          <div class="singles" v-for="item in this.toutiao" :key='item'>
            <a class="new" v-if="item.rank<4">
              <div class="single">
                <span class="seq_highlight">{{item.rank}}</span>
                <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                <span class="more">{{item.more}}</span>
              </div>
            </a>
            <a class="new" v-else>
              <div class="single">
                <span class="seq">{{item.rank}}</span>
                <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                <span class="more">{{item.more}}</span>
              </div>
            </a>
          </div>
        </div>
        <div class="tw-footer">
          <a href="https://www.toutiao.com/" class="link">
            <span>今日头条</span>
          </a>
          <el-button icon="el-icon-arrow-up" mini circle @click="show_toutiao"></el-button>
        </div>
      </div>
    </div>
      </div>
<!--科技模块-->
      <div class="keji">
<!--头部-->
        <div class="items_header">
          <span class="big_title">科技</span>
          <el-button type="primary" v-if="this.keji_data==='展开分类'" class="showAll" icon="el-icon-bottom" @click="show_keji">{{keji_data}}</el-button>
          <el-button type="primary" v-else class="showAll" icon="el-icon-arrow-up" @click="show_keji">{{keji_data}}</el-button>
        </div>
        <!--        每行-->
        <div class="items_row">
<!--果壳-->
          <div v-if="guokr_xianshi" class="grid-content" @click="show_guokr">
            <img src="../assets/logo/guokr.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/guokr.png" class="small_logo">
              <span class="category">科学人</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.guokr" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.guokr.com/" class="link">
                <span>果壳</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_guokr"></el-button>
            </div>
          </div>
<!--36氪-->
          <div v-if="kr36_xianshi" class="grid-content" @click="show_36kr">
            <img src="../assets/logo/36kr.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/36kr.png" class="small_logo">
              <span class="category">24小时热榜</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.kr36" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.36kr.com/" class="link">
                <span>36氪</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_36kr"></el-button>
            </div>
          </div>
<!--yc-->
          <div v-if="yc_xianshi" class="grid-content" @click="show_yc">
            <img src="../assets/logo/yc.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/yc.png" class="small_logo">
              <span class="category">hacker news</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.yc" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://news.ycombinator.com/news" class="link">
                <span>yc</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_yc"></el-button>
            </div>
          </div>
        </div>
      </div>
<!--视频模块-->
      <div class="shipin">
        <!--        头部-->
        <div class="items_header">
          <span class="big_title">视频</span>
          <el-button type="primary" v-if="this.shipin_data==='展开分类'" class="showAll" icon="el-icon-bottom" @click="show_shipin">{{shipin_data}}</el-button>
          <el-button type="primary" v-else class="showAll" icon="el-icon-arrow-up" @click="show_shipin">{{shipin_data}}</el-button>
        </div>
        <!--        每行-->
        <div class="items_row">
<!--澎湃-->
          <div v-if="pengpai_xianshi" class="grid-content" @click="show_pengpai">
            <img src="../assets/logo/pengpai.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/pengpai.png" class="small_logo">
              <span class="category">视频</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.pengpai" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.thepaper.cn/" class="link">
                <span>澎湃</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_pengpai"></el-button>
            </div>
          </div>
<!--梨子视频-->
          <div v-if="pearvideo_xianshi" class="grid-content" @click="show_pearvideo">
            <img src="../assets/logo/pearvideo.png" class="logos">
          </div>
          <div v-else class="details">
            <div class="tw-header">
              <img src="../assets/logo/pearvideo.png" class="small_logo">
              <span class="category">总榜</span>
            </div>
            <div class="tw-main">
              <div class="singles" v-for="item in this.pearvideo" :key='item'>
                <a class="new" v-if="item.rank<4">
                  <div class="single">
                    <span class="seq_highlight">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
                <a class="new" v-else>
                  <div class="single">
                    <span class="seq">{{item.rank}}</span>
                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>
                    <span class="more">{{item.more}}</span>
                  </div>
                </a>
              </div>
            </div>
            <div class="tw-footer">
              <a href="https://www.pearvideo.com/" class="link">
                <span>梨视频</span>
              </a>
              <el-button icon="el-icon-arrow-up" mini circle @click="show_pearvideo"></el-button>
            </div>
          </div>
<!--哔哩哔哩-->
<!--          <div v-if="bilibili_xianshi" class="grid-content" @click="show_bilibili">-->
<!--            <img src="../assets/logo/bilibili.png" class="logos">-->
<!--          </div>-->
<!--          <div v-else class="details">-->
<!--            <div class="tw-header">-->
<!--              <img src="../assets/logo/bilibili.png" class="small_logo">-->
<!--              <span class="category">日排行</span>-->
<!--            </div>-->
<!--            <div class="tw-main">-->
<!--              <div class="singles" v-for="item in this.bilibili" :key='item'>-->
<!--                <a class="new" v-if="item.rank<4">-->
<!--                  <div class="single">-->
<!--                    <span class="seq_highlight">{{item.rank}}</span>-->
<!--                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>-->
<!--                    <span class="more">{{item.more}}</span>-->
<!--                  </div>-->
<!--                </a>-->
<!--                <a class="new" v-else>-->
<!--                  <div class="single">-->
<!--                    <span class="seq">{{item.rank}}</span>-->
<!--                    <span class="title" @click="goPage(item.url)">{{item.title}}</span>-->
<!--                    <span class="more">{{item.more}}</span>-->
<!--                  </div>-->
<!--                </a>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="tw-footer">-->
<!--              <a href="https://www.bilibili.com/" class="link">-->
<!--                <span>哔哩哔哩</span>-->
<!--              </a>-->
<!--              <el-button icon="el-icon-arrow-up" mini circle @click="show_bilibili"></el-button>-->
<!--            </div>-->
<!--          </div>-->
        </div>
      </div>
      <div class="footer-text">小组成员：王旭东，滕达，王逸康</div>
    </el-main>
<!--    尾部-->
<!--    <el-footer>小组成员：王旭东，滕达，王逸康</el-footer>-->
  </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      timeForm: {
        date: ''
      },
      pickerOptions: {
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      },
      cur_time: '',
      baidu: [],
      baidu_xianshi: true,
      weibo: [],
      weibo_xianshi: true,
      zhihu: [],
      zhihu_xianshi: true,
      wangyi: [],
      wangyi_xianshi: true,
      qdaily: [],
      qdaily_xianshi: true,
      search360: [],
      search360_xianshi: true,
      toutiao: [],
      toutiao_xianshi: true,
      guokr: [],
      guokr_xianshi: true,
      kr36: [],
      kr36_xianshi: true,
      yc: [],
      yc_xianshi: true,
      pengpai: [],
      pengpai_xianshi: true,
      pearvideo: [],
      pearvideo_xianshi: true,
      bilibili: [],
      bilibili_xianshi: true,
      zonghe_data: '展开分类',
      keji_data: '展开分类',
      shipin_data: '展开分类'
    }
  },
  methods: {
    logout () {
      // window.sessionStorage.clear()
      // this.$router.push('/login')
      console.log(this.cur_time)
    },
    getSearch () {
      this.timeForm.date = this.cur_time
      const { data: res } = this.$http.post('url', this.timeForm)
      if (res.status_code !== 200) { return this.$message.error('搜索失败') } else {
        this.$message.success('搜索成功，正在跳转')
        this.$router.push('/')
      }
    },
    show_zonghe () {
      if (this.zonghe_data === '展开分类') {
        this.zonghe_data = '收起分类'
        this.baidu_xianshi = true
        this.weibo_xianshi = true
        this.zhihu_xianshi = true
        this.wangyi_xianshi = true
        this.qdaily_xianshi = true
        this.toutiao_xianshi = true
        this.show_baidu()
        this.show_weibo()
        this.show_zhihu()
        this.show_wangyi()
        this.show_qdaily()
        this.show_toutiao()
      } else {
        this.zonghe_data = '展开分类'
        // this.baidu_xianshi = !this.baidu_xianshi
        // this.weibo_xianshi = !this.weibo_xianshi
        // this.zhihu_xianshi = !this.zhihu_xianshi
        // this.wangyi_xianshi = !this.wangyi_xianshi
        // this.qdaily_xianshi = !this.qdaily_xianshi
        // this.toutiao_xianshi = !this.toutiao_xianshi
        this.baidu_xianshi = true
        this.weibo_xianshi = true
        this.zhihu_xianshi = true
        this.wangyi_xianshi = true
        this.qdaily_xianshi = true
        this.toutiao_xianshi = true
      }
    },
    show_keji () {
      if (this.keji_data === '展开分类') {
        this.keji_data = '收起分类'
        this.guokr_xianshi = true
        this.kr36_xianshi = true
        this.yc_xianshi = true
        this.show_guokr()
        this.show_36kr()
        this.show_yc()
      } else {
        this.keji_data = '展开分类'
        // this.guokr_xianshi = !this.guokr_xianshi
        // this.kr36_xianshi = !this.kr36_xianshi
        // this.yc_xianshi = !this.yc_xianshi
        this.guokr_xianshi = true
        this.kr36_xianshi = true
        this.yc_xianshi = true
      }
    },
    show_shipin () {
      if (this.shipin_data === '展开分类') {
        this.shipin_data = '收起分类'
        this.pengpai_xianshi = true
        this.pearvideo_xianshi = true
        this.bilibili_xianshi = true
        this.show_pengpai()
        this.show_pearvideo()
        this.show_bilibili()
      } else {
        this.shipin_data = '展开分类'
        // this.pengpai_xianshi = !this.pengpai_xianshi
        // this.pearvideo_xianshi = !this.pearvideo_xianshi
        // this.bilibili_xianshi = !this.
        this.pengpai_xianshi = true
        this.pearvideo_xianshi = true
        this.bilibili_xianshi = true
      }
    },
    async show_baidu () {
      this.timeForm.date = this.cur_time
      console.log(this.timeForm.date)
      const { data: res } = await this.$http.post('zonghe/baidu', this.timeForm)
      this.baidu = res.hot.data
      this.baidu_xianshi = !this.baidu_xianshi
    },
    async show_weibo () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('zonghe/weibo', this.timeForm)
      this.weibo = res.data
      this.weibo_xianshi = !this.weibo_xianshi
    },
    async show_zhihu () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('zonghe/zhihu', this.timeForm)
      this.zhihu = res.hot.data
      this.zhihu_xianshi = !this.zhihu_xianshi
    },
    async show_wangyi () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('zonghe/wangyi', this.timeForm)
      this.wangyi = res.data
      this.wangyi_xianshi = !this.wangyi_xianshi
    },
    async show_qdaily () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('zonghe/qdaily', this.timeForm)
      this.qdaily = res.data
      this.qdaily_xianshi = !this.qdaily_xianshi
    },
    async show_toutiao () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('zonghe/toutiao', this.timeForm)
      this.toutiao = res.data
      this.toutiao_xianshi = !this.toutiao_xianshi
    },
    async show_guokr () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('keji/guokr', this.timeForm)
      this.guokr = res.data
      this.guokr_xianshi = !this.guokr_xianshi
    },
    async show_36kr () {
      this.timeForm.date = this.cur_time
      console.log(this.timeForm.date)
      const { data: res } = await this.$http.post('keji/kr36', this.timeForm)
      this.kr36 = res.data
      this.kr36_xianshi = !this.kr36_xianshi
    },
    async show_yc () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('keji/yc', this.timeForm)
      this.yc = res.data
      this.yc_xianshi = !this.yc_xianshi
    },
    async show_pengpai () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('shipin/pengpai', this.timeForm)
      this.pengpai = res.data
      this.pengpai_xianshi = !this.pengpai_xianshi
    },
    async show_pearvideo () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('shipin/pearvideo', this.timeForm)
      this.pearvideo = res.data
      this.pearvideo_xianshi = !this.pearvideo_xianshi
    },
    async show_bilibili () {
      this.timeForm.date = this.cur_time
      const { data: res } = await this.$http.post('shipin/bilibili', this.timeForm)
      this.bilibili = res.data
      this.bilibili_xianshi = !this.bilibili_xianshi
    },
    // async show_baidu () {
    //   const { data: res } = await this.$http.get('zonghe/baidu')
    //   this.baidu = res.hot.data
    //   this.baidu_xianshi = !this.baidu_xianshi
    // },
    // async show_weibo () {
    //   const { data: res } = await this.$http.get('zonghe/weibo')
    //   this.weibo = res.data
    //   this.weibo_xianshi = !this.weibo_xianshi
    // },
    // async show_zhihu () {
    //   const { data: res } = await this.$http.get('zonghe/zhihu')
    //   this.zhihu = res.hot.data
    //   this.zhihu_xianshi = !this.zhihu_xianshi
    // },
    // async show_wangyi () {
    //   const { data: res } = await this.$http.get('zonghe/wangyi')
    //   this.wangyi = res.data
    //   this.wangyi_xianshi = !this.wangyi_xianshi
    // },
    // async show_qdaily () {
    //   const { data: res } = await this.$http.get('zonghe/qdaily')
    //   this.qdaily = res.data
    //   this.qdaily_xianshi = !this.qdaily_xianshi
    // },
    // async show_toutiao () {
    //   const { data: res } = await this.$http.get('zonghe/toutiao')
    //   this.toutiao = res.data
    //   this.toutiao_xianshi = !this.toutiao_xianshi
    // },
    // async show_guokr () {
    //   const { data: res } = await this.$http.get('keji/guokr')
    //   this.guokr = res.data
    //   this.guokr_xianshi = !this.guokr_xianshi
    // },
    // async show_36kr () {
    //   const { data: res } = await this.$http.post('keji/kr36', this.cur_time)
    //   this.kr36 = res.data
    //   this.kr36_xianshi = !this.kr36_xianshi
    // },
    // async show_yc () {
    //   const { data: res } = await this.$http.get('keji/yc')
    //   this.yc = res.data
    //   this.yc_xianshi = !this.yc_xianshi
    // },
    // async show_pengpai () {
    //   const { data: res } = await this.$http.get('shipin/pengpai')
    //   this.pengpai = res.data
    //   this.pengpai_xianshi = !this.pengpai_xianshi
    // },
    // async show_pearvideo () {
    //   const { data: res } = await this.$http.get('shipin/pearvideo')
    //   this.pearvideo = res.data
    //   this.pearvideo_xianshi = !this.pearvideo_xianshi
    // },
    // async show_bilibili () {
    //   const { data: res } = await this.$http.get('shipin/bilibili')
    //   this.bilibili = res.data
    //   this.bilibili_xianshi = !this.bilibili_xianshi
    // },
    goPage (url) {
      window.location.href = url
    }
  }
}
</script>

<style lang="less" scoped>
  .el-header {
    background-color: #ffffff;
    color: #333;
    display: flex;
    text-align: center;
    line-height: 60px;
    align-items: center;
    font-size: 20px;
  }

  .el-footer {
    background-color: #f3f0f0;
    display: block;
    color: #333;
    text-align: center;
    line-height: 60px;
    font-size: 62.5%;
  }

  .el-main {
    background-color: #faf8f8;
    color: #333;
    text-align: center;
    vertical-align: middle;
  }

  .home-container {
    height: 100%;
  }

  .logo_pic {
    max-height: 150px;
    max-width: 150px;
    /*height: 100%;*/
    /*width: 100%;*/
    position: absolute;
    top: 6px;
  }

  .wenzi-header {
    position: absolute;
    left: 180px;
    top: 0;
  }

  .searchButton {
    position: absolute;
    right: 150px;
  }

  .logOutButton {
    position: absolute;
    right: 20px;
  }

  .time-select {
    position: absolute;
    right: 100px;
    top: 0;
  }

  .el-row {
    margin-bottom: 25px;
    justify-content: space-around;
    display: flex;
    &:last-child {
      margin-bottom: 0;
    }
   }

  .el-col {
    border-radius: 4px;
  }

  .grid-content {
    border-radius: 4px;
    width: 25%;
    height: 50px;
    background: #ffffff;
    display: flex;
    align-items:center;
    justify-content: space-around;
    vertical-align: middle;
    cursor: pointer;
  }

  .grid-content-hidden {
    border-radius: 4px;
    width: 25%;
    height: 50px;
    background: #faf8f8;
    display: flex;
    align-items:center;
    justify-content: space-around;
    vertical-align: middle;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

  .page-component__scroll .el-scrollbar__wrap {
    overflow-x: auto;
  }

  .footer-text {
    background-color: #faf8f8;
    display: block;
    color: #333;
    text-align: center;
    line-height: 60px;
    font-size: 62.5%;
  }

  .items_header {
    text-align: center;
    line-height: 40px;
    font-size: 30px;
    display: flex;
    justify-content: center;
    box-sizing: border-box;
    margin-top: 20px;
  }

  .showAll {
    font-size: 15px;
    margin-left: 10px;
  }

  .logos {
    height: 35px;
  }

  .items_row {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }

  .details {
    width: 25%;
    height: 410px;
    background-color: #eeeeee;
  }

  .tw-header {
    background-color: #ffffff;
    color: #333;
    display: flex;
    align-items:center;
    height: 10%;
    justify-content: space-between;
  }

  .tw-footer {
    background-color: #ffffff;
    color: #333;
    text-align: center;
    display: flex;
    align-items:center;
    justify-content: space-between;
    height: 10%;
  }

  .tw-main {
    background-color: #ffffff;
    color: #333;
    text-align: center;
    height: 80%;
    overflow: auto;
  }

  .small_logo {
    height: 30px;
    padding-left: 5px;
  }

  .category {
    justify-content: right;
    padding-right: 10px;
  }

  .singles {
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    -webkit-box-pack: justify;
    justify-content: space-between;
  }

  .single {
    display: flex;
    justify-content: space-between;
    /*-webkit-box-align: center;*/
    /*align-items: center;*/
    width: 100%;
    font-size: .85rem;
    padding-top: 10px;
  }

  .new {
    text-decoration: none;
    color: #050404;
    display: flex;
    justify-content: space-between;
    font-family: Microsoft YaHei,Arial,Helvetica,sans-serif;
  }

  .from {
    color: #323131;
  }

  .link {
    color: #2d2929;
    text-decoration: none;
    margin-left: 10px;
  }

  .seq_highlight {
    color: #3db4f1;
    font-style: italic;
    width: 10%;
    text-align: center;
    /*margin-right: 10px;*/
  }

  .seq {
    font-style: italic;
    width: 10%;
    text-align: center;
    /*margin-right: 10px;*/
  }

  .title{
    width: 65%;
    text-align: left;
    cursor: pointer;
  }

  .more {
    width: 20%;
    padding-right: 0;
    /*margin-right: 10px;*/
    text-align: center;
    float: right;
  }
</style>
