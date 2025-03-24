@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to edit your profile.', 'warning')
        return redirect(url_for('index'))

    card = Card.query.filter_by(user_id=user_id).first()
    if not card:
        flash('No profile found for this user.', 'warning')
        return redirect(url_for('create_card'))

    form = CardForm(obj=card)
    if form.validate_on_submit():
        file = form.photo.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            card.photo = filename

        card.first_name = form.first_name.data
        card.last_name = form.last_name.data
        card.middle_name = form.middle_name.data
        card.birth_date = form.birth_date.data.strftime('%Y-%m-%d') if form.birth_date.data else None
        card.phone = form.phone.data
        card.email = form.email.data
        card.instagram = form.instagram.data
        card.telegram = form.telegram.data
        card.facebook = form.facebook.data
        card.whatsapp = form.whatsapp.data
        card.address = form.address.data

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('view_card', card_id=card.id))
    return render_template('edit_profile.html', form=form, card=card)