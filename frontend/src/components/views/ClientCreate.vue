<template>
    <div class="create-client">
        <b-container>
            <b-row class="justify-content-md-center">
            <b-col md="6">
                <b-card title="Crear Cliente">
                <b-form @submit.prevent="handleSubmit">
                    <b-form-group label="Nombre:" label-for="name">
                    <b-form-input
                        id="name"
                        v-model="client.name"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group label="Número de documento:" label-for="document_id">
                    <b-form-input
                        id="document_id"
                        v-model="client.document_id"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group label="Dirección:" label-for="address">
                    <b-form-input
                        id="address"
                        v-model="client.address"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group label="Teléfono:" label-for="phone">
                    <b-form-input
                        id="phone"
                        v-model="client.phone"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group label="Email:" label-for="email">
                    <b-form-input
                        id="email"
                        v-model="client.email"
                        type="email"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group label="Contraseña:" label-for="password">
                    <b-form-input
                        id="password"
                        v-model="client.password"
                        type="password"
                        required
                    ></b-form-input>
                    </b-form-group>
    
                    <b-form-group>
                    <b-button type="submit" variant="primary">Crear Cliente</b-button>
                    </b-form-group>
                </b-form>
                </b-card>
            </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import VAPI from '@/http_common';
import { HTTP_STATUS, SERVICE_NAMES } from "@/app_constants";

export default {
    data() {
        return {
        client: {
            name: '',
            document_id: '',
            address: '',
            phone: '',
            email: '',
            password: ''
        }
        };
    },
    methods: {
        async handleSubmit() {
        try {
            const response = await VAPI.post(`${SERVICE_NAMES.USER}/clients`, this.client);
            if (response.status === HTTP_STATUS.CREATED) {
                this.$toast.success('Cliente creado exitosamente');
                this.$router.push('/');
            }
        } catch (error) {
            this.$toast.error('Error al crear el cliente');
        }
        }
    }
};
</script>

<style scoped>
.create-client {
    margin-top: 20px;
}
</style>
