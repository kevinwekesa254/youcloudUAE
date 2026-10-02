# Rebuilds the Pricing and Add-ons sections of index.html, and their Arabic keys in js/i18n.js,
# from tools/pricing_data.py. Run: python3 tools/build_pricing.py
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
from pricing_data import SEGMENTS, ADDONS, DH

NOTE_EN = ('<b>Software is licensed per store, per month</b> — one licence covers every till in that store. '
           'Billed annually, excl. VAT. Hardware is one-time. <b>Payments MDR 2–3% extra</b>, card terminal required. '
           'Move up any time, no re-integration.')
NOTE_AR = ('<b>تُرخَّص البرمجيات لكل متجر شهرياً</b> — ترخيص واحد يغطي كل صناديق الدفع في المتجر. '
           'تُدفع سنوياً، ولا تشمل ضريبة القيمة المضافة. الأجهزة بدفعة واحدة. <b>رسوم الخصم على المدفوعات 2–3% إضافية</b>، ويلزم جهاز بطاقات. '
           'رقِّ باقتك في أي وقت دون إعادة تكامل.')
ar = {
  'h.pr.eyebrow': 'الأسعار · الإمارات',
  'h.pr.title': 'كل شيء مشمول. بالدرهم. بلا مفاجآت.',
  'h.pr.lead': 'باقات لكل متجر شهرياً، تُدفع سنوياً. ابدأ مجاناً وادفع لكل طلب، أو احصل على طلبات بلا حدود مع الباقة المتقدمة.',
  'h.pr.popular': 'الأكثر طلباً',
  'h.pr.per': '/متجر/شهرياً',
  'h.pr.custom': 'مخصّص',
  'h.pr.talk': 'سعر حسب حجم فروعك',
  'h.pr.note': NOTE_AR,
  'c.onetime': 'دفعة واحدة',
}
o = []
o.append('''    <!-- Pricing -->
    <section class="section" id="pricing" style="padding-top:0">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow" data-i18n="h.pr.eyebrow">Pricing · UAE</span>
          <h2 class="h2" data-i18n="h.pr.title">All in. In AED. No surprises.</h2>
          <p class="lead" data-i18n="h.pr.lead">Packages per store, per month, billed annually. Start free and pay per order, or go unlimited on Power.</p>
        </div>
        <div class="seg-toggle reveal" role="tablist" aria-label="Business type">
          <span class="pill" aria-hidden="true"></span>''')
for i, seg in enumerate(SEGMENTS):
    k = 'h.pr.seg.' + seg['id']; ar[k] = seg['ar']
    o.append(f'          <button type="button" role="tab" id="tab-{seg["id"]}" aria-controls="plans-{seg["id"]}" aria-selected="{"true" if i == 0 else "false"}" data-seg="{seg["id"]}" data-i18n="{k}">{seg["en"]}</button>')
o.append('        </div>')

for i, seg in enumerate(SEGMENTS):
    compact = seg.get('compact')
    o.append(f'        <div class="plans" id="plans-{seg["id"]}" role="tabpanel" aria-labelledby="tab-{seg["id"]}"{"" if i == 0 else " hidden"}>')
    o.append(f'          <div class="price-grid{" compact" if compact else ""}">')
    for j, p in enumerate(seg['plans']):
        b = f'h.pr.{seg["id"]}.{p["key"]}'
        ar[b + '.n'] = p['name'][1]; ar[b + '.p'] = p['who'][1]; ar[b + '.m'] = p['meta'][1]
        pop = p.get('popular')
        delay = f' style="--d:{j * 0.1:.1f}s"' if j else ''
        o.append(f'            <article class="price-card{" pop" if pop else ""} reveal"{delay}>')
        if pop: o.append('              <span class="badge" data-i18n="h.pr.popular">Most popular</span>')
        o.append(f'              <span class="tag" data-i18n="{b}.n">{p["name"][0]}</span>')
        if p['price'] is None:
            o.append('              <div class="price upper" data-i18n="h.pr.custom">Custom</div>')
            o.append('              <p class="price-note" data-i18n="h.pr.talk">Priced to your estate</p>')
        else:
            o.append(f'              <div class="price">{DH}{p["price"]} <small data-i18n="h.pr.per">/store/mo</small></div>')
            ar[b + '.note'] = p['note'][1]
            o.append(f'              <p class="price-note" data-i18n="{b}.note">{p["note"][0]}</p>')
        o.append(f'              <p data-i18n="{b}.p">{p["who"][0]}</p>')
        o.append(f'              <p class="price-meta" data-i18n="{b}.m">{p["meta"][0]}</p>')
        if p['feats']:
            ar[b + '.f0'] = p['head'][1]
            o.append('              <ul class="feat">')
            o.append(f'                <li data-i18n="{b}.f0">{p["head"][0]}</li>')
            for n, (en, a) in enumerate(p['feats'], 1):
                ar[f'{b}.f{n}'] = a
                o.append(f'                <li data-i18n="{b}.f{n}">{en}</li>')
            o.append('              </ul>')
        if p['price'] is None:
            o.append('              <a class="btn btn-primary" href="enterprise.html#contact" data-i18n="c.contactent">Contact enterprise</a>')
        else:
            o.append(f'              <button class="btn {"btn-white" if pop else "btn-primary"}" data-demo data-i18n="c.bookdemo">Book a demo</button>')
        o.append('            </article>')
    o.append('          </div>')

    if compact:
        hw, pay, ft = seg['hardware'], seg['payments'], seg['features']
        s = 'h.pr.ss'
        ar[s + '.hw.t'] = hw['tag'][1]; ar[s + '.hw.s'] = hw['sub'][1]
        o.append('          <div class="ss-extras">')
        o.append('            <article class="ss-card ss-hw reveal">')
        o.append(f'              <span class="tag" data-i18n="{s}.hw.t">{hw["tag"][0]}</span>')
        o.append('              <div class="ss-hw-top">')
        o.append('                <img src="images/desktop_-_1_12.webp" alt="y7000 self-service kiosk" loading="lazy" width="1536" height="1024">')
        o.append(f'                <div><h3>{hw["name"]}</h3><p data-i18n="{s}.hw.s">{hw["sub"][0]}</p>'
                 f'<div class="hw-price">{DH}{hw["price"]}<small data-i18n="c.onetime">one-time</small></div></div>')
        o.append('              </div>')
        o.append('              <div class="specs">')
        for n, ((lk, la), (vk, va)) in enumerate(hw['specs']):
            ar[f'{s}.sp{n}l'] = la; ar[f'{s}.sp{n}v'] = va
            o.append(f'                <div><span data-i18n="{s}.sp{n}l">{lk}</span><b data-i18n="{s}.sp{n}v">{vk}</b></div>')
        o.append('              </div>')
        o.append('            </article>')
        ar[s + '.ft.t'] = ft['tag'][1]
        o.append('            <article class="ss-card ss-ft reveal" style="--d:.1s">')
        o.append(f'              <span class="tag" data-i18n="{s}.ft.t">{ft["tag"][0]}</span>')
        o.append('              <ul class="ticks">')
        for n, (en, a) in enumerate(ft['items']):
            ar[f'{s}.ft{n}'] = a
            o.append(f'                <li data-i18n="{s}.ft{n}">{en}</li>')
        o.append('              </ul>')
        o.append('            </article>')
        ar[s + '.pay.t'] = pay['tag'][1]; ar[s + '.pay.u'] = pay['unit'][1]; ar[s + '.pay.x'] = pay['text'][1]
        o.append('            <article class="ss-card ss-pay reveal" style="--d:.2s">')
        o.append(f'              <span class="tag" data-i18n="{s}.pay.t">{pay["tag"][0]}</span>')
        o.append(f'              <div class="ss-rate">{pay["rate"]} <small data-i18n="{s}.pay.u">{pay["unit"][0]}</small></div>')
        o.append(f'              <p data-i18n="{s}.pay.x">{pay["text"][0]}</p>')
        o.append('            </article>')
        o.append('          </div>')
    o.append('        </div>')

o.append(f'''        <p class="footnote reveal" data-i18n="h.pr.note">{NOTE_EN}</p>
      </div>
    </section>

''')

# Add-ons
ar.update({
  'h.ad.eyebrow': 'الإضافات · اختيارية',
  'h.ad.title': 'فعّل المزيد عندما تكون مستعداً.',
  'h.ad.lead': 'جميع الإضافات تعمل على بيانات التاجر نفسها. أضف واحدة هذا الربع، وأخرى في الربع التالي — دون إعادة تكامل.',
  'h.ad.note': 'أسعار المدفوعات لكل معاملة — رسوم خصم البطاقات (فيزا / ماستركارد / أمريكان إكسبريس) 2–3%، المحافظ المحلية 0.9–1.5%، شبكات الدفع عبر QR من 0.5 إلى 1.2%. تُحتسب فوق رسوم البرمجيات ويلزم جهاز بطاقات. خصومات حسب الحجم في باقة المؤسسات. جميع الأسعار لا تشمل ضريبة القيمة المضافة 5%.',
})
o.append('''    <!-- Add-ons -->
    <section class="section" id="addons" style="padding-top:0">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow" data-i18n="h.ad.eyebrow">Add-ons · optional</span>
          <h2 class="h2" data-i18n="h.ad.title">Turn on more when you're ready.</h2>
          <p class="lead" data-i18n="h.ad.lead">All add-ons run on the same merchant data. Add one this quarter, another next — no re-integration.</p>
        </div>
        <div class="addons reveal">''')
for n, (name, pen, par) in enumerate(ADDONS, 1):
    ar[f'h.ad.p{n}'] = par
    o.append(f'          <div><h4>{name}</h4><p data-i18n="h.ad.p{n}">{pen}</p></div>')
o.append('''        </div>
        <p class="footnote reveal" data-i18n="h.ad.note">Payment rates per transaction — card MDR (Visa / Mastercard / Amex) 2–3%, domestic wallets 0.9–1.5%, QR rails 0.5–1.2%. Charged on top of software · card terminal required. Volume discounts on Enterprise. All prices excl. 5% VAT.</p>
      </div>
    </section>

''')
html = '\n'.join(o)

p = os.path.join(ROOT, 'index.html'); s = open(p).read()
a = s.index('    <!-- Pricing -->'); z = s.index('    <!-- FAQ -->')
s = s[:a] + html + s[z:]
open(p, 'w').write(s)

p = os.path.join(ROOT, 'js/i18n.js'); s = open(p).read()
s = re.sub(r"\n    (?:'|\")h\.(?:pr|ad)\.[^'\"]*(?:'|\"): [^\n]*,", '', s)
s = re.sub(r"\n    /\* Pricing \(generated by tools/build_pricing\.py\) \*/", '', s)
s = re.sub(r"\n    'c\.onetime': [^\n]*,", '', s)
block = ''.join(f"\n    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}," for k, v in ar.items())
s = s.replace("    /* Add-ons */", "    /* Pricing & add-ons (generated by tools/build_pricing.py) */" + block + "\n\n    /* Add-ons */", 1)
open(p, 'w').write(s)
print('ok', len(ar), 'arabic keys')
