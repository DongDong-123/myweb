  /*公共导航部分--------------------------------------*/
  //顶部导航鼠标经过出现内容
  function topNav(){
    for(var i =1;i<5;i++){
      $('.layout-header-nav li').eq(i).mouseover(function(){
        var $this = $('.layout-header-nav-child');
        var lw = $('.layout-header-nav-child-list li').width();
        var t = $('.layout-header-nav-child-list li').length;
        var uw = lw * t /2;
        $this.show();
        $this.find('.layout-header-nav-child-list').css('margin-left',-uw);
        }).mouseout(function(){
          $('.layout-header-nav-child').hide();
        });
    }
 }//顶部导航鼠标经过出现内容 E

  function topLogin(){
      // 登录图片鼠标经过
      $('#layoutHeaderUser').mouseover(function(){
        $('.layout-user-downmenu').show();
      }).mouseout(function() {
          $('.layout-user-downmenu').hide();
      });
  }
  // 公共返回顶部
  function backTop(){
    $(window).scroll(function(){
      var dTop = $(document).scrollTop();
      var fTop = $('.layout-header .navbar').height();
      if(dTop >fTop){
        $('.layout-magnet').show();
      }else{
        $('.layout-magnet').hide();
      }
    });
    $(".layout-magnet").click(function(){
      $("html").animate({"scrollTop": "0px"},500); //IE,FF
      $("body").animate({"scrollTop": "0px"},500); //Webkit
    });
  } 
  /*---------------------------------------------------*/ 

  /*首页部分-------------------------------------------*/
  // 首页侧导航鼠标经过出现内容
  function leftNav(){
    $('#homeCategory li').mouseover(function(){
      $(this).find('.home-category-child').show();
    }).mouseout(function(){
      $(this).find('.home-category-child').hide();
    })
  }

  /*---------------------------------------------------*/ 

  /*全部商品部分---------------------------------------*/
  function comPro(){
    $(".gl-item").mouseover(function(){
      $(this).find('.compare-btn-list').css('display','block');
    });
    $(".gl-item").mouseout(function(){
      $(this).find('.compare-btn-list').css('display','none');
    });

  }

  /*---------------------------------------------------*/ 

  /*产品详情页部分-------------------------------------*/
  function  detaNav(){
    $('#detailFast ul li').click(function(){
      var t = $(this).index();
      
      $('#detailFast ul li').addClass('current').siblings().removeClass('current');
      $('.detail-content div').eq(t).addClass('current').siblings().removeClass('current');
    })
      $(window).scroll(function(){
        var dt = $('#detail').offset().top;
        var dTop = $(document).scrollTop();
        if(dTop >= dt){
          $('#detailFast').addClass('float-nav');
        }else{
          $('#detailFast').removeClass('float-nav');
        }
        //console.log(dt,dTop)
      })
    } 
     // 数量增加减少
    function addMin(){
      // 减少
      $('.vm-minus').click(function(){
          var n=$('#J_quantity').val();
          var num=parseInt(n)-1;
          if(num<=1){ 
            $('.vm-minus').addClass('disabled');
            $(this).next().val(1);
          }else{
            $('.vm-minus').removeClass('disabled');
            $(this).next().val(num);
          }
          
      })
      //增加
      $('.vm-plus').click(function(){
          var n=$('#J_quantity').val();
          var num=parseInt(n)+1;
          if(num>1){ $('.vm-minus').removeClass('disabled');}
          if(num>5){ return;}
            $(this).prev().val(num);
          })
      }// 数量增加减少E
  

/*购物车--------------------------------------------*/ 
var buyid = []
var buynum
// var goodstotal = document.getElementById('totalPrice')
// var Goodstotal = goodstotal.innerHTML;
// console.log('Goodstotal',Goodstotal)
// console.log('goodstotal',goodstotal,typeof(goodstotal))
var danprice=0
var dannum=0
var zongprice = 0
var zongprices = 0

// function alltoatl(){

// }

// function tests(){
//     $('.mz-checkbox').click(function(){
//         console.log('触发')
//             console.log('总价',zongprices)
//         // var numms = $('.cart-col-select2 .checked').length
//         if($(this).hasClass('.checked')){
    
//         }
//         // console.log('numms',numms)
    
//     })
//     }
//选择框操作
function allSelect(){
 
  var aee = false;
  var see = false;
  var lis = {}
  // 全选
    $('.JSelectAll .mz-checkbox').click(function(){
        if(aee == false){
            $('.JSelectAll .mz-checkbox').addClass('checked');
            console.log('a')
            $('.cart-col-select2 .mz-checkbox').addClass('checked');
            console.log('b')
            aee = true;
        }else{
            $('.JSelectAll .mz-checkbox').removeClass('checked');
            $('.cart-col-select2 .mz-checkbox').removeClass('checked');
            $('#totalPrice').html('0.00');
            console.log('c')
            aee = false;
        };
    });
  
    //单选
    $('.cart-col-select2 .mz-checkbox').click(function(){
        // 单选切换
        $(this).toggleClass('checked');
        // 获取选中商品的索引
        var selectindex = $(this).parents('.cart-product').index()
        // buyid.push(selectindex)
        // buynum= buyid.length
        // console.log('buynum1',buynum)
        // console.log('buyid',buyid)
        // console.log('selectindex',selectindex,typeof(selectindex))
        // 选中商品的数量
        var count = $(".cart-col-select2 .checked").length;
        console.log('count1',count)
        // 所有商品的数量
        var countall = $(".cart-col-select2").length;
        console.log('count2',countall)
        // 当所有商品都被单击选中时
        if(count==countall){
            // 选中全选
            $('.JSelectAll .mz-checkbox').addClass('checked');

        }else{
            $('.JSelectAll .mz-checkbox').removeClass('checked');

    };
    // 计算选中商品数量和总价
    // 获取当前索引
    var fzhi=$(this).parents('.cart-product').index();
    // 获取单价对象
    var $nPrice = $('.cart-product').eq(fzhi).find('.cart-col-price .cart-product-price');
    // 单个商品单价
    var npText = parseInt($nPrice.text());
    // 获取数量对象
    var $nInput = $('.cart-product').eq(fzhi).find('.mz-adder-input');
    console.log('$nInput',$nInput)
    // 获取商品的数量
    var n=$nInput.val();
    // 商品数量转为数字类型
    var num=parseInt(n);
    // 单个商品小计
    zongprice = npText * num
    
    lis[fzhi] = zongprice
    console.log(lis)
    // 底部总价
    zongprices = zongprices+zongprice
    // $('#totalPrice').text() = zongprices
    console.log('zongprices',zongprices)
    $('#totalPrice').html(zongprices);


    // console.log('danprice',danprice)
    // console.log('dannum',dannum)
    console.log('zongprice',zongprice)
    nums = buyid.length
    // console.log('nums',nums,typeof(nums))
    // var sinTotals = Number($(this).parents('.cart-product').children().find('.cart-product-price ').text())
    // console.log('sinTotals',sinTotals,typeof(sinTotals))
    });
    $('.mz-checkbox').change(function(){
        $(this).parents('.cart-product').children('.total')
        // if(){}

    })
};

// 数量增加减少
function cartAddMin(){
      var pList = $('.cart-product');
      console.log('pList',pList.length)
      // console.log('buynum2',buynum)
      //选中商品数量
      var count = $(".cart-col-select2 .checked");
      console.log('count2',count.length)

      //页面底部显示初始值
      //初始商品总数量
       

      $('#totalCount').html(count);
        // 初始商品总价格
      $('#totalPrice').html('0.00');


      var fsnC = Number( $('#totalCount').text());
      console.log('fsnC',fsnC)

      //初始商品总和
      var i = 0;
      var fsPrice = 0;

      while(i<pList.length){
        // var v = pList.eq(i).index();
        var sPrice=Number($('.cart-product').eq(i).find('.cart-product-price .total').text());
        console.log('sPrice',sPrice)

        var fsPrice = Number(fsPrice)+Number(sPrice);
        console.log('fsPrice',fsPrice)
        
        i++;
        // $('#totalPrice').html(fsPrice+'.00');
      }

      
      // 减少
       //检测操作的是哪个商品
      $('.mz-adder-subtract').click(function(){
            // 获取当前操作商品元素的索引
           var fzhi=$(this).parents('.cart-product').index();
           // var reg=/^pro\d$/;
           // var prod=reg.exec(fzhi);
           // console.log('fzhi',fzhi)

           //商品展示个数、减号、超过数量的文本(对象)

           var $mText = $('.cart-product').eq(fzhi).find('.cart-product-number-max');
           // console.log('$mText',$mText)
           var $nSub = $('.cart-product').eq(fzhi).find('.mz-adder-subtract');
           var $nInput = $('.cart-product').eq(fzhi).find('.mz-adder-input');

           // var selectNum =$('.cart-product').eq(fzhi).find('.mz-adder-input');
           // 商品数量
           // var n=$nInput.val();
           var n=$nInput.val();
           // console.log('nss',n,typeof(n))
           var num=parseInt(n)-1;
           dannum = num
           // console.log('num',num,typeof(num))


           //获取当前商品的单价
           // var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');
           var $nPrice = $('.cart-product').eq(fzhi).find('.cart-col-price .cart-product-price');
           // 转为数字类型
           var npText = parseInt($nPrice.text());
           danprice = npText
           // console.log('npText',npText,typeof(npText))
           // 获取当前商品的合计
           var $sumPrice = $('.cart-product').eq(fzhi).find('.cart-col-total .cart-product-price');
           var spText = parseInt($sumPrice.text());

           //单个商品的小计
           spText= spText - npText;
           console.log('spText',spText,typeof(spText))
           if(spText<=0){
            spText = 0;
            $sumPrice.html(spText+'.00');
           console.log('单个小计1',spText)

           }else{
            $sumPrice.html(spText+'.00');
           console.log('单个小计2',spText)
           }
            
           
           //商品减少操作
           if(num<=0){ 
              $nInput.val(0);
              $nSub.addClass('disabled');

              // return
           }else if(num>0){
              $nSub.removeClass('disabled');
              $nInput.val(num);
           }
           if(num<5){
              $mText.removeClass('show');
           }

        //    //页面底部显示一共多少商品和选择的商品个数
        //    var fsNum = Number( $('#totalCount').text());
        //    var newNum = fsNum-1;
        //    $('#totalCount').html(newNum);

        //    //页面底部总和
        //    var fPrice=$('#totalPrice').text();
        //    var regs=/\d+/;
        //    var sfPrice= Number(regs.exec(fPrice));

        //    //算出新的总价格
        //    var nsfPrice=spText+sfPrice;
        //    if(nsfPrice<=0){
        //     nsfPrice = 0;
        //    $('#totalPrice').html(nsfPrice+'.00');
        //    console.log('减少1',nsfPrice)
        //    }else{
        //    $('#totalPrice').html(nsfPrice+'.00');
        //    console.log('减少2',nsfPrice)
        // }

      })
      //增加
      $('.mz-adder-add').click(function(){
           //检测操作的是哪个商品
           var fzhi=$(this).parents('.cart-product').index();
           var reg=/^pro\d$/;
           var prod=reg.exec(fzhi);
           // console.log('fzhi',fzhi)

           //商品展示个数、加号、超过数量的文本
           var $nAdd = $('.cart-product').eq(fzhi).find('.mz-adder-add');
           // var $nSub = $('.cart-product').eq(fzhi).find('.mz-adder-add');
           var $nInput = $('.cart-product').eq(fzhi).find('.mz-adder-input');
           var n=$nInput.val();
           var $mText = $('.cart-product').eq(fzhi).find('.cart-product-number-max');
           var num=parseInt(n)+1;
           // console.log('num',num,typeof(num))
           // console.log('$nAdd',$nAdd,typeof($nAdd))

           //获取当前商品的单价和小计
           var $nPrice = $('.cart-product').eq(fzhi).find('.cart-col-price .cart-product-price');
           var npText = parseInt($nPrice.text());
           // console.log('npText',npText,typeof(npText))
           
           var $sumPrice = $('.cart-product').eq(fzhi).find('.cart-col-total  .cart-product-price');
           var spText = parseInt($sumPrice.text());

           
           //商品增加操作
           if(num<5){ 
                $nAdd.removeClass('disabled');
                $mText.removeClass('show');
                // $mText.text();
                $nInput.val(num);
           }
           if(num==5){
                $nAdd.addClass('disabled');
                $mText.addClass('show');
                $mText.text("限购5件");
                $nInput.val(num);
           } 
           if(num>5){ 
                $nAdd.addClass('disabled');
                $mText.addClass('show');
                $mText.text("限购5件");
                $nInput.val(5);
                return false;
           }
           //单个商品的小计
           spText= spText + npText;
           console.log('spText',spText,typeof(spText))

           $sumPrice.html(spText+'.00');
           
           // console.log(num);

           // //页面底部显示一共多少商品和选择的商品个数
           // var fsNum = Number( $('#totalCount').text());
           // var newNum = fsNum+1;
           // $('#totalCount').html(newNum);


           // //页面底部总和
           // var fPrice=$('#totalPrice').text();
           // var regs=/\d+/;
           // var sfPrice= Number(regs.exec(fPrice));


           // //算出新的总价格
           // var nsfPrice=spText+sfPrice;
           // $('#totalPrice').html(nsfPrice+'.00');
           // console.log('nsfPrice',nsfPrice)
        })




    
  

      //叉号删除商品

    $('.cart-product-remove').click(function(){
          // //获取商品个数
          // var geshu=Number($(this).parents('.zhanshi1').find('.yi1').text());
          // //获取商品价格
          // var dqjinbi=$(this).parents('.zhanshi1').find('.jiage').text();
          // var reg=/\d+/;
          // var dqjb=Number(reg.exec(dqjinbi));
          // //获取总共价格
          // var zgjinbi=$('.jine').find('h4 span').text();
          // var regs=/\d+/;
          // var zgjb=Number(regs.exec(zgjinbi));
          // //求出新的价格
          // var newjinbi=zgjb-dqjb*geshu;
          // //赋值
          // $('.jine').find('h4 span').html(newjinbi+'.00');
          // //求出商品个数
          // var gs=Number($('.zg h5 span').text());
          // var newgs=gs-geshu;
          // $('.zg h4 span').html(newgs);
          // $('.zg h5 span').html(newgs);
          $(this).parents('.cart-product').remove();
    })

    
}// 数量增加减少E 





/*---------------------------------------------------*/ 



/*登录页面----------------------------------------*/ 
function nLogin(){
      //   提交
      var nameOk=false;
      var paddOk=false;
      //获取焦点事件
     $('input[name=account]').focus(function(){
          //添加颜色
          $('.cycode-box').addClass('btn-focus');
          $('.passwd-box').removeClass('btn-focus');
     })
     $('input[name=password]').focus(function(){
          $('.cycode-box').removeClass('btn-focus');
          $('.passwd-box').addClass('btn-focus');
     })
     //丧失焦点事件
     $('input[name=account]').blur(function(){
          //获取用户信息进行正则获取
          var v =$(this).val();
          var reg=/^\d{6,18}$/;
          //判断如果为true则通过
          if(reg.test(v)){
                $('.cycode-box').removeClass('btn-error');
                $('.tip-box').addClass('visiblility-hidden');
                nameOk=true;
          }else{
                $('.cycode-box').addClass('btn-error');
                $('.tip-box').removeClass('visiblility-hidden');
                $('.tip-box .tip-font').html("请输入合法的手机号码")
                nameOk=false;
          }
          console.log(v)
     })
      //丧失焦点事件
     $('input[name=password]').blur(function(){
          //获取用户信息
          var v =$(this).val();
          var reg=/^\w{6,18}$/;
          //判断如果为true则通过
          if(reg.test(v)){
                $('.passwd-box').removeClass('btn-error');
                $('.tip-box').addClass('visiblility-hidden');
                passOk=true;
          }else{
                $('.passwd-box').addClass('btn-error');
                $('.tip-box').removeClass('visiblility-hidden');
                $('.tip-box .tip-font').html("请输入正确的密码")
                passOk=false;
          }
          console.log(v)
     })
}




/*---------------------------------------------------*/ 