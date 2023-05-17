<template>
    <div class="grid">
        <div class="col-12 md:col-6">
            <div class="card">
                <h5>Generar CodigoQR de un producto</h5>
                <div class="p-fluid formgrid grid">
                    <div class="field col-12">
                        <label for="sku">Folio:</label>
                        <InputText id="sku" type="text" v-model="idsku"/>
                    </div>
                    <div class="field col-12">
                        <label for="nombre">Producto:</label>
                        <InputText id="nombre" type="text" v-model="nombreP" />
                    </div>
                    <div class="field col-12">
                        <label for="precio">Precio:</label>
                        <InputNumber id="precio" v-model="precios" :minFractionDigits="2" :maxFractionDigits="5"/>
                    </div>
                    <div class="field col-12 md:col-6">
                        <Button label="Generar Código QR" class="p-button-success mr-2 mb-2" @click="QR()"  v-tooltip="'Click al presionar'"></Button>
                    </div>
                </div>              
            </div>
        </div>
        <div v-if="showQR" class="col-12 md:col-6">
            <div class="card">
                <qrcode-vue :value="value" :size="size" level="H" />
            </div>
        </div>
        
        <Toast/>
    </div>
</template>

<script>
import QrcodeVue from 'qrcode.vue'
import { defineComponent } from 'vue';

export default defineComponent({

    data() {
      return {
        idsku: '',
        nombreP: '',
        precios: '',
        value: '',
        size: 200,
        showQR: false,
      }
    },
    methods: {
        QR(){
            if (this.idsku === '' || this.nombreP === '' || this.precios === '') {
                this.$toast.add({severity:'error', summary: 'Error al generar el Codigo QR', detail: 'Tienes Campos Vacios', life: 5000});
            } else {
                this.value ="Folio: "+this.idsku+"\nNombre del producto: "+this.nombreP+"\nPrecio: $"+this.precios;
                this.showQR = true;
            }
        }
    },
    components: {
      QrcodeVue,
    },
});
</script>