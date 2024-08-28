<template>
    <div class="login-container">
        <b-container>
            <b-row class="justify-content-md-center">
                <b-col md="4">
                    <b-card title="Login" class="mt-3">
                        <b-form @submit.prevent="handleSubmit">
                            <b-form-group label="Email:" label-for="email">
                                <b-form-input
                                    id="email"
                                    v-model="email"
                                    type="email"
                                    required
                                ></b-form-input>
                            </b-form-group>
            
                            <b-form-group label="Password:" label-for="password">
                                <b-form-input
                                    id="password"
                                    v-model="password"
                                    type="password"
                                    required
                                ></b-form-input>
                            </b-form-group>
            
                            <b-form-group>
                                <b-button type="submit" variant="primary">Login</b-button>
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
            email: '',
            password: ''
        }
    },
    methods: {
        async handleSubmit(){
            try {
                const response = await VAPI.post(`${SERVICE_NAMES.AUTH}/login`, {
                    email: this.email,
                    password: this.password
                })
                if (response.status === HTTP_STATUS.OK) {
                    this.$toast.success('Welcome');
                    this.$router.push('/home')
                }
            } catch (error) {
                this.$toast.error('Invalid email or password');
            }
        }
    }
}
</script>

<style scoped>
.login-container {
    margin-top: 20px;
}
</style>
