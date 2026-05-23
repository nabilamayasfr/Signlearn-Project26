from flask import Blueprint, render_template, request, redirect, url_for, flash, session


web = Blueprint("web", __name__)


@web.route("/")
def index():
    user = {
        "name": session.get("user_name", "Ara Signlearn")
    }

    mastered = 12
    total = 26
    pct = round((mastered / total) * 100)

    return render_template(
        "pages/index.html",
        user=user,
        mastered=mastered,
        total=total,
        pct=pct
    )


@web.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_input = request.form.get("login")
        password = request.form.get("password")

        if login_input == "admin" and password == "admin123":
            session["user_name"] = "Admin SignLearn"
            session["role"] = "admin"

            flash("Login berhasil", "success")
            return redirect(url_for("web.index"))

        elif login_input == "user" and password == "user123":
            session["user_name"] = "User SignLearn"
            session["role"] = "user"

            flash("Login berhasil", "success")
            return redirect(url_for("web.index"))

        else:
            flash("Email/nama pengguna atau kata sandi salah", "error")

    return render_template("pages/login.html")


@web.route("/logout")
def logout():
    session.clear()
    flash("Kamu berhasil keluar", "success")
    return redirect(url_for("web.login"))


@web.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nama_lengkap = request.form.get("nama_lengkap")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        if not nama_lengkap or not username or not email or not password or not password_confirmation:
            flash("Semua data wajib diisi, kecuali nomor telepon", "error")
            return render_template("pages/register.html")

        if password != password_confirmation:
            flash("Konfirmasi kata sandi tidak sesuai", "error")
            return render_template("pages/register.html")

        if len(password) < 6:
            flash("Kata sandi minimal 6 karakter", "error")
            return render_template("pages/register.html")

        flash("Pendaftaran berhasil. Silakan masuk.", "success")
        return redirect(url_for("web.login"))

    return render_template("pages/register.html")


@web.route("/pembelajaran")
def pembelajaran():
    return render_template("pages/quiz.html")


@web.route("/latihan")
def latihan():
    return render_template("pages/quiz.html")


@web.route("/detection")
def detection():
    return render_template("pages/detection.html")


@web.route("/history")
def history():
    return render_template("pages/history.html")


@web.route("/faq")
def faq():
    return "Halaman FAQ"

@web.route("/profile")
def profile():
    user = {
        "name": session.get("user_name", "Arabella")
    }

    return render_template("pages/profile.html", user=user)