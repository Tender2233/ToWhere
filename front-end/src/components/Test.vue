<template>
  <div class="weibo">
    <div class="tw-header">
      <img src="../assets/logo/weibo.png" class="small_logo">
      <span class="category">热榜</span>
    </div>
    <div class="tw-main">
      <div class="singles" v-for="item in this.baidu" :key='item'>
        <a :href=item.url class="new" v-if="item.rank<4">
          <div class="single">
            <span class="seq_highlight">{{item.rank}}</span>
            <span class="title">{{item.title}}</span>
            <span class="more">{{item.more}}</span>
          </div>
        </a>
        <a :href=item.url class="new" v-else>
          <div class="single">
          <span class="seq">{{item.rank}}</span>
          <span class="title">{{item.title}}</span>
          <span class="more">{{item.more}}</span>
          </div>
        </a>
      </div>
    </div>
    <div class="tw-footer">
      <a href="https://www.weibo.com" class="link">
        <span>微博</span>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      baidu: [
        {
          rank: 1,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 2,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 3,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 4,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 5,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 6,
          title: '吉林封闭小区居民用蔬菜摆感谢语吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 7,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 8,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 9,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 10,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 1,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 2,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 3,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 4,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 5,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 6,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 7,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 8,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 9,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        },
        {
          rank: 10,
          title: '吉林封闭小区居民用蔬菜摆感谢语',
          more: '999782',
          url: 'https://www.baidu.com'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
  .weibo {
    width: 25%;
    height: 410px;
    background-color: #eeeeee;
  }

  .tw-header {
    background-color: #B3C0D1;
    color: #333;
    display: flex;
    align-items:center;
    height: 10%;
    justify-content: space-between;
  }

  .tw-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    display: flex;
    align-items:center;
    justify-content: space-between;
    height: 10%;
  }

  .tw-main {
    background-color: #E9EEF3;
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
    cursor: pointer;
    text-decoration: none;
    color: #050404;
    display: flex;
    justify-content: space-between;
    font-family: Microsoft YaHei,Arial,Helvetica,sans-serif;
  }

  .link {
    color: #050404;
    text-decoration: none;
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
  }

  .more {
    width: 20%;
    padding-right: 0;
    /*margin-right: 10px;*/
    text-align: center;
    float: right;
  }
</style>
