const {createApp} = Vue

const TaskApp={
    data(){
        return{
            barang:{
                'namaBarang':'',
                'merk':'',
                'tipe':''
            },
            daftarBarang: []
        }
    },
    async created(){
        await this.getDaftarBarang()
    },
    methods:{
        async sendRequest(url, method, data){
            const myHeaders = new Headers({
                'Content-Type': 'application/json',
                'X-Requested-Width':'XMLHttpRequest'
            })

            const response = await fetch(url,{
                method: method,
                headers: myHeaders,
                body: data
            })
            return response
        },
        async getDaftarBarang(){
            const response = await this.sendRequest(window.location, 'get')
            this.daftarBarang = await response.json()
        }
    },
    delimiters: ['[',']']
}

createApp(TaskApp).mount('#app')