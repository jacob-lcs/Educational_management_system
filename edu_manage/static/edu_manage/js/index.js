new Vue({
    el: '#app',
    data: {
        visible: false
    },
    methods: {
        show: function () {
            this.visible = true;
        }
    }
})

new Vue({
    el: "#app2",
    data: {
        message: "你好啊"
    }
})

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.id +1}}.{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: '蔬菜' },
      { id: 1, text: '奶酪' },
      { id: 2, text: '随便其它什么人吃的东西' }
    ]
  }
})
