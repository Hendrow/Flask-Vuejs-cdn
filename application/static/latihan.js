const {createApp} = Vue

const TaskApp={
    data(){
        return{
            barang:{
                'namaBarang':'',
                'merk':'',
                'tipe':'',
                'sn':'',
                'status':''
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
        },
        async addBarang(){
            await this.getDaftarBarang()
            await this.sendRequest(window.location + 'add', 'post', JSON.stringify(this.barang))
            await this.getDaftarBarang()
            this.barang.namaBarang = ''
            this.barang.merk = ''
            this.barang.tipe = ''
            this.barang.sn = ''
            this.barang.status = ''
        }
    },
    delimiters: ['[',']']
}

createApp(TaskApp).mount('#app')