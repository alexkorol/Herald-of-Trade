package com.bluelithalo.poetrends.view

import android.graphics.Color
import android.view.View
import android.widget.ImageView
import android.widget.TextView
import com.bluelithalo.poetrends.R
import com.bluelithalo.poetrends.model.Overview
import com.bluelithalo.poetrends.model.item.ItemOverview
import com.squareup.picasso.Picasso

class BaseTypeViewHolder : PoeNinjaViewHolder
{
    var baseTypeNameTextView: TextView
    var baseTypeIconImageView: ImageView

    var baseTypeChaosValueAffix: TextView
    var baseTypeExaltValueAffix: TextView

    var baseTypeValueChange: TextView

    var baseTypeLevelTextView: TextView
    var baseTypeModImageView: ImageView

    constructor(v: View) : super(v)
    {
        baseTypeNameTextView = v.findViewById<View>(R.id.base_type_name_text_view) as TextView
        baseTypeIconImageView = v.findViewById<View>(R.id.base_type_icon_image_view) as ImageView

        baseTypeChaosValueAffix = v.findViewById<View>(R.id.base_type_chaos_value_affix) as TextView
        baseTypeExaltValueAffix = v.findViewById<View>(R.id.base_type_exalt_value_affix) as TextView

        baseTypeValueChange = v.findViewById<View>(R.id.base_type_value_change) as TextView

        baseTypeLevelTextView = v.findViewById<View>(R.id.base_type_level_text_view) as TextView
        baseTypeModImageView = v.findViewById<View>(R.id.base_type_mod_image_view) as ImageView
    }

    override fun configureViewHolder(overview: Overview?, position: Int)
    {
        val baseTypeOverview = overview as ItemOverview
        val baseTypeLine = baseTypeOverview?.lines?.let { it[position] }

        baseTypeLine?.let {
            var iconUrl = it.icon

            it.variant?.let {
                if (it.equals("Elder")) {
                    baseTypeModImageView.setImageResource(R.drawable.ic_elder)
                    iconUrl += "&elder=1"
                }
                else if (it.equals("Shaper")) {
                    baseTypeModImageView.setImageResource(R.drawable.ic_shaper)
                    iconUrl += "&shaper=1"
                }
            } ?: run {
                baseTypeModImageView.setImageResource(android.R.color.transparent)
            }

            Picasso.get()
                .load(iconUrl)
                .placeholder(R.drawable.load_placeholder_skill_gem)
                .error(R.drawable.load_error_skill_gem)
                .into(baseTypeIconImageView)

            val chaosValueAffixText = String.format("%.1f", it.chaosValue) + " \u00D7"
            val exaltValueAffixText = String.format("%.1f", it.exaltedValue) + " \u00D7"
            val baseTypeLevelText = if (it.levelRequired ?: 0 >= 86) "86+" else "${it.levelRequired}"
            baseTypeNameTextView.text = it.name
            baseTypeChaosValueAffix.text = chaosValueAffixText
            baseTypeExaltValueAffix.text = exaltValueAffixText
            baseTypeLevelTextView.text = baseTypeLevelText

            it.sparkline?.totalChange?.let {
                val valueChangeText = (if (it > 0.0) "+" else "") + String.format("%.1f", it) + "%"
                baseTypeValueChange.text = valueChangeText
                baseTypeValueChange.setTextColor(if (it >= 0.0) Color.GREEN else Color.RED)
            }
        } ?: run {
            baseTypeIconImageView.setImageResource(R.drawable.load_error_skill_gem)
            baseTypeNameTextView.text = "N/A"
            baseTypeChaosValueAffix.text = "N/A \u00D7"
            baseTypeExaltValueAffix.text = "N/A \u00D7"
            baseTypeLevelTextView.text = "X"
            baseTypeValueChange.text = "N/A"
            baseTypeValueChange.setTextColor(Color.GRAY)
        }
    }
}