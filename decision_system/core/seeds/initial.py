from core.models import Category, SubCategory, CategoryCriterion


def run():

    # Clear old data (optional but useful during development)
    Category.objects.all().delete()

    # ============================
    # Create Categories
    # ============================

    product = Category.objects.create(name="Product Purchase")
    tech = Category.objects.create(name="Technological Decision")
    career = Category.objects.create(name="Career Decision")
    travel = Category.objects.create(name="Travel Decision")
    hiring = Category.objects.create(name="Hiring Decision")
    financial = Category.objects.create(name="Financial Decision")

    # ============================
    # Subcategories
    # ============================

    vehicles = SubCategory.objects.create(category=product, name="Vehicles")
    digital = SubCategory.objects.create(category=product, name="Digital Products")
    assets = SubCategory.objects.create(category=product, name="Assets")
    consumables = SubCategory.objects.create(category=product, name="Consumables")
    services= SubCategory.objects.create(category=product, name="Services")

    tech_stack = SubCategory.objects.create(category=tech, name="Tech Stack Selection")

    education = SubCategory.objects.create(category=career, name="Education")
    employment = SubCategory.objects.create(category=career, name="Employment")
    skill = SubCategory.objects.create(category=career, name="Skill Development")
    entrepreneurship = SubCategory.objects.create(category=career, name="Entrepreneurship")

    travel_general = SubCategory.objects.create(category=travel, name="Travel")

    hiring_sub = SubCategory.objects.create(category=hiring, name="Candidate Evaluation")

    investment = SubCategory.objects.create(category=financial, name="Investments")
    loan = SubCategory.objects.create(category=financial, name="Loans")

    # ============================
    # Criteria Insertion
    # ============================

    # Vehicles
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=vehicles, name="Price Efficiency"),
        CategoryCriterion(subcategory=vehicles, name="Mileage"),
        CategoryCriterion(subcategory=vehicles, name="Service Availability"),
        CategoryCriterion(subcategory=vehicles, name="After Sale Value"),
        CategoryCriterion(subcategory=vehicles, name="Maintenance Ease"),
        CategoryCriterion(subcategory=vehicles, name="Ergonomics"),
    ])

    # Digital Products
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=digital, name="Cost Efficiency"),
        CategoryCriterion(subcategory=digital, name="Performance"),
        CategoryCriterion(subcategory=digital, name="Reliability"),
        CategoryCriterion(subcategory=digital, name="User Experience"),
        CategoryCriterion(subcategory=digital, name="Service Availability"),
        CategoryCriterion(subcategory=digital, name="Reviews & Reputation"),
    ])

    # Assets
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=assets, name="Liquidity"),
        CategoryCriterion(subcategory=assets, name="Long Term Value"),
        CategoryCriterion(subcategory=assets, name="Future Potential"),
        CategoryCriterion(subcategory=assets, name="Tax Efficiency"),
        CategoryCriterion(subcategory=assets, name="Seller Assurance"),
    ])

    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=consumables, name="Price per Unit Efficiency"),
        CategoryCriterion(subcategory=consumables, name="Quality"),
        CategoryCriterion(subcategory=consumables, name="Brand Reputation"),
        CategoryCriterion(subcategory=consumables, name="Promotional Offers"),
        CategoryCriterion(subcategory=consumables, name="Availability"),
        CategoryCriterion(subcategory=consumables, name="Past Experience"),
        CategoryCriterion(subcategory=consumables, name="Health Impact"),
    ])
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=services, name="Cost Efficiency"),
        CategoryCriterion(subcategory=services, name="Ease of cancellation"),
        CategoryCriterion(subcategory=services, name="Customer Support"),
        CategoryCriterion(subcategory=services, name="Service Quality"),
        CategoryCriterion(subcategory=services, name="Secuirty & Privacy"),
    ])
    #Travel Decision
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=travel_general, name="Cost Efficiency"),
        CategoryCriterion(subcategory=travel_general, name="Vibe & Experience"),
        CategoryCriterion(subcategory=travel_general, name="Amenities & Comfort"),
        CategoryCriterion(subcategory=travel_general, name="Safety"),
        CategoryCriterion(subcategory=travel_general, name="Ease of Travel"),
        CategoryCriterion(subcategory=travel_general, name="Community & Culture"),
    ])
    # Tech Stack
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=tech_stack, name="Cost Efficiency"),
        CategoryCriterion(subcategory=tech_stack, name="Scalability"),
        CategoryCriterion(subcategory=tech_stack, name="Reliability"),
        CategoryCriterion(subcategory=tech_stack, name="Community Support"),
        CategoryCriterion(subcategory=tech_stack, name="Maintenance Ease"),
        CategoryCriterion(subcategory=tech_stack, name="Infrastructure Compatibility"),
        CategoryCriterion(subcategory=tech_stack, name="Team Skill Alignment"),
        CategoryCriterion(subcategory=tech_stack, name="Existing Resources"),
    ])

    # Hiring
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=hiring_sub, name="Technical Skills"),
        CategoryCriterion(subcategory=hiring_sub, name="Experience"),
        CategoryCriterion(subcategory=hiring_sub, name="Communication Skills"),
        CategoryCriterion(subcategory=hiring_sub, name="Cultural Fit"),
        CategoryCriterion(subcategory=hiring_sub, name="Growth Potential"),
        CategoryCriterion(subcategory=hiring_sub, name="Retention Potential"),
        CategoryCriterion(subcategory=hiring_sub, name="Reliability"),
        CategoryCriterion(subcategory=hiring_sub, name="Salary"),
    ])

    # Investments
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=investment, name="Expected Return"),
        CategoryCriterion(subcategory=investment, name="Risk Safety"),
        CategoryCriterion(subcategory=investment, name="Liquidity"),
        CategoryCriterion(subcategory=investment, name="Time Horizon Suitability"),
        CategoryCriterion(subcategory=investment, name="Cost Efficiency"),
        CategoryCriterion(subcategory=investment, name="Tax Efficiency"),
    ])

    # Loans
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=loan, name="Total Repayment Efficiency"),
        CategoryCriterion(subcategory=loan, name="Interest Rate Advantage"),
        CategoryCriterion(subcategory=loan, name="EMI Comfort"),
        CategoryCriterion(subcategory=loan, name="Prepayment Flexibility"),
    ])

    # Entrepreneurship
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=entrepreneurship, name="Market Potential"),
        CategoryCriterion(subcategory=entrepreneurship, name="Competitive Advantage"),
        CategoryCriterion(subcategory=entrepreneurship, name="Financial Viability"),
        CategoryCriterion(subcategory=entrepreneurship, name="Scalability"),
        CategoryCriterion(subcategory=entrepreneurship, name="Team Strength"),
        CategoryCriterion(subcategory=entrepreneurship, name="Personal Passion & Fit"),
        CategoryCriterion(subcategory=entrepreneurship, name="Risk Tolerance Alignment"),
        CategoryCriterion(subcategory=entrepreneurship, name="Ease of Entry"),
    ])

    #Eduacation
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=education, name="Job Opportunities"),
        CategoryCriterion(subcategory=education, name="Curriculum Relevance & Quality"),
        CategoryCriterion(subcategory=education, name="Cost Efficiency"),
        CategoryCriterion(subcategory=education, name="Flexibility & Time Commitment"),
        CategoryCriterion(subcategory=education, name="Reputation"),
        CategoryCriterion(subcategory=education, name="Networking Opportunities"),
        CategoryCriterion(subcategory=education, name="Personal Growth & Interest Alignment"),
        CategoryCriterion(subcategory=education, name="Campus Infrastructure & Resources"),
    ])

     # Employment
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=employment, name="Salary & Benefits"),
        CategoryCriterion(subcategory=employment, name="Career Growth Opportunities"),
        CategoryCriterion(subcategory=employment, name="Work-Life Balance"),
        CategoryCriterion(subcategory=employment, name="Company Culture & Values"),
        CategoryCriterion(subcategory=employment, name="Job Security"),
        CategoryCriterion(subcategory=employment, name="Location & Commute"),
        CategoryCriterion(subcategory=employment, name="Role & Responsibilities Alignment"),
        CategoryCriterion(subcategory=employment, name="Management & Leadership Quality"),
        CategoryCriterion(subcategory=employment, name="Company Reputation"),
        CategoryCriterion(subcategory=employment, name="Tenure & Stability"),
    ])

        # Skill Development
    CategoryCriterion.objects.bulk_create([
        CategoryCriterion(subcategory=skill, name="Career Advancement Potential"),
        CategoryCriterion(subcategory=skill, name="Personal Interest & Passion Alignment"),
        CategoryCriterion(subcategory=skill, name="Cost Efficiency"),
        CategoryCriterion(subcategory=skill, name="Time Commitment & Flexibility"),
        CategoryCriterion(subcategory=skill, name="Skill Relevance & Demand"),
        CategoryCriterion(subcategory=skill, name="Learning Resources Quality"),
        CategoryCriterion(subcategory=skill, name="Community & Networking Opportunities"),
        CategoryCriterion(subcategory=skill, name="Certification & Recognition"),
        CategoryCriterion(subcategory=skill, name="Learning Curve"),
    ])
    print("Initial decision tree inserted successfully!")