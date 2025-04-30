import streamlit as st
import json
import os
from utils import authenticate_user, register_user, add_login_page_css

def show_login_page():
    # Add custom CSS to hide sidebar only on login page
    add_login_page_css()
    
    st.title("Connexion")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Create tabs for login and sign up
        tab1, tab2 = st.tabs(["Connexion", "Créer un compte"])
        
        with tab1:
            with st.form("login_form"):
                st.subheader("Veuillez vous connecter")
                username = st.text_input("Nom d'utilisateur")
                password = st.text_input("Mot de passe", type="password")
                submitted = st.form_submit_button("Se connecter")
                
                if submitted:
                    if authenticate_user(username, password):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.success("Connexion réussie!")
                        st.rerun()
                    else:
                        st.error("Nom d'utilisateur ou mot de passe invalide")
        
        with tab2:
            with st.form("signup_form"):
                st.subheader("Créer un nouveau compte")
                new_username = st.text_input("Choisir un nom d'utilisateur")
                new_password = st.text_input("Choisir un mot de passe", type="password")
                confirm_password = st.text_input("Confirmer le mot de passe", type="password")
                email = st.text_input("Email (optionnel)")
                submitted_signup = st.form_submit_button("S'inscrire")
                
                if submitted_signup:
                    if not new_username or not new_password:
                        st.error("Veuillez remplir tous les champs obligatoires")
                    elif new_password != confirm_password:
                        st.error("Les mots de passe ne correspondent pas")
                    else:
                        result = register_user(new_username, new_password, email)
                        if result == "success":
                            st.success("Compte créé avec succès! Vous pouvez maintenant vous connecter.")
                        elif result == "exists":
                            st.error("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
                        else:
                            st.error("Une erreur s'est produite lors de la création du compte.")

# Main app flow
